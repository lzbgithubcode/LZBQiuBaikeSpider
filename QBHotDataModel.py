class HotDataModel(object):
    #用户名称
    user_name = ''

    #用户年龄
    user_age = 0

    #用户头像
    user_img = ''

    #用户发布内容
    publish_content = ''

    #点赞数量
    praise_count = 0

    #评论数量
    comment_count = 0

    def log(self):
        print(self.user_name,self.user_age,self.user_img,self.publish_content,self.praise_count,self.comment_count)


