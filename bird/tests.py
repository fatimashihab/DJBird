def get_likes(user, self):
    likes = Likes.objects.filter(user__user__username=user, update=self.pk)
    return likes


def get_likers(self):
    likes = self.get_likes()
    likers = []
    for like in likes:
        likers.append(like.user)
    return likers



def like_update(request):
    request = values["like_update"]
    if values["liked"]:
            x = Likes.objects.filter(update=request.POST["like"],user__user__username=values["user"])
            x.delete()
            values["liked"] = False
    else:
            like_method = Likes()
            like_method.user = values["user"]
            like_method.follows = User.objects.get(user__username=request.POST["like"])
            like_method.save()
            values["liked"] = True
    values["img"] = User.objects.get(user__username=request.POST["Follow"]).img
    values["search"] = User.objects.get(user__username=request.POST["Follow"])
    values["Updates"] = Update.objects.filter(user__user__username=request.POST['Follow']).order_by('-created_on')
    resp = render_to_response("index.html", values, context_instance=RequestContext(request))
    return resp


def fatma():
    if Follows.objects.filter(follows__user__username=values["tofollow"],
                              user__user__username=request.user).count() > 0:
        values["following"] = True
    else:
        values["following"] = False

    if values["following"]:
        x = Follows.objects.filter(follows__user__username=request.POST.get("following"),
                                   user__user__username=values["user"])
        x.delete()
        values["following"] = False
    else:
        follow_method = Follows()
        follow_method.user = values["user"]
        follow_method.follows = User.objects.filter(user__username="sumayashihab")[0]
        follow_method.save()
        values["following"] = True




    ENDDDD

    if request.POST.get("Update"):  # test the form type
            form = SendUpdates(request.POST)
            if User.objects.filter(user__username=request.user.username).count() > 0:
                values["img"] = User.objects.filter(user__username=request.user.username)[0]
            new_update = Update(text=request.POST['Update'])
            user = User.objects.filter(user__username =request.user)[0]
            new_update.user = user
            new_update.save()
            values["Updates"] = Update.objects.all().order_by('-created_on')[:50]
            return render_to_response("index.html", values, context_instance=RequestContext(request))

        elif request.POST.get("Search"):
            form = SearchUsers(request.POST)


            if form.is_valid():
                values["search"] = request.POST['Search']
                if User.objects.filter(user__username=request.POST["Search"]).count() > 0:
                    values["img"]= User.objects.get(user__username=request.POST["Search"]).img
                    values["Updates"]=Update.objects.filter(user__user__username=request.POST['Search']).order_by('-created_on')
                    if Follows.objects.filter(follows__user__username=request.POST["Search"],user__user__username=request.user).count()>0 :
                        values["following"]=True
                    else:
                        values["following"]=False
                    return render_to_response("User.html", values, context_instance=RequestContext(request))

                else:
                    if User.objects.filter(user__username=request.user.username).count() > 0:
                        values["img"] = User.objects.filter(user__username=request.user.username)[0]

                    values["error"]=["NO USER ACCOUNTS MATCHING SEARCH QUERY. PLEASE, TRY AGAIN . . "]
                    values["Updates"] = Update.objects.all().order_by('-created_on')[:50]
                    return render_to_response("index.html", values, context_instance=RequestContext(request))


    if request.POST.get("Follow"):
            values["user"] = User.objects.filter(user__username=request.user)[0]
            values["tofollow"] = request

            if Follows.objects.filter(follows__user__username=request.POST["Follow"],user__user__username=request.user).count()>0:
                   values["following"] = True
            else:
                values["following"] = False

            resp= follow_user(values)
            return resp
        #if request.POST.get["like"]:
        #    values["user"]=User.objects.filter(user__username=request.user)[0]
        #    values["like_update"]=request
        #    if Likes.objects.filter(update=request.POST["Like"],user__user__username=request.user).count()>0:
        #        values["liked"]=True
        #    else:
        #        values["liked"]=False
        #    resp=like_update(values)
        #    return resp

