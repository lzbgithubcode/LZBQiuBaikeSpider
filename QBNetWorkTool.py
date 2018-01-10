
from urllib import request,error
import ssl
from lxml import etree

import QBHotDataModel

#配置请求参数
page = 1
url = 'https://www.qiushibaike.com/hot/page/' + str(page)

#配置请求头
user_agent ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
request_headers = {'User-Agent':user_agent}

#开始请求
def startRequestHTMLQiushiBaikeList(reqUrl,requestHeaders):
    """
    网络请求数据
    :param reqUrl:   string 请求的地址
    :param request_headers:  {} 请求头
    :return:  请求的包含html标签的字符串
    """

    req = request.Request(reqUrl,headers=requestHeaders)
    #请求ssl禁掉这个证书
    context = ssl._create_unverified_context()

    with request.urlopen(req,context=context) as response:
        html_response = response.read().decode('utf-8')
        return html_response


#请求结果处理
def hanleNetworkCallBackHTMLResponse(html_response):

    content = etree.HTML(html_response)

    #获取热门的内容段子
    # nodes = content.xpath('//div[@class="article block untagged mb15 typs_hot"]')
    nodes = content.xpath('//div[@id="content-left"]/div[@class]')

    datalist = []
    #获取数据
    for element in nodes:

        #创建模型
        hotObject = QBHotDataModel.HotDataModel()

        # 获取头像
        res_icomImg = element.xpath('div[@class="author clearfix"]/a[1]/img/@src')[0]
        res_icomImg = "https:" + res_icomImg
        hotObject.user_img = res_icomImg


        #获取用户名
        res_author = element.xpath('div[@class="author clearfix"]/a[2]/h2[1]')[0]
        hotObject.user_name = res_author.text

        #获取年龄
        res_age = element.xpath('div[@class="author clearfix"]/div[1]')[0]
        hotObject.user_age = res_age.text

        #获取段子的内容
        res_content = element.xpath('a[1]/div[1]/span[1]')[0]
        hotObject.publish_content = res_content.text

        #获取点赞数量
        res_praiseCount = element.xpath('div[@class ="stats"]/span[@class="stats-vote"]/i[1]')[0]
        hotObject.praise_count = res_praiseCount.text

        #获取评论数量
        res_commentCount = element.xpath('div[@class ="stats"]/span[@class="stats-comments"]/a[1]/i[1]')[0]
        hotObject.comment_count = res_commentCount.text

        #拼接数组
        datalist.append(hotObject)

    return datalist

#1.开始请求
html = startRequestHTMLQiushiBaikeList(url,request_headers)

#2.请求结果处理
datalist = hanleNetworkCallBackHTMLResponse(html)

for model in datalist:
    model.log()






"""

初级段子手I
 24 https://pic.qiushibaike.com/system/avtnew/1477/14770806/thumb/20180107081740.JPEG?imageView2/1/w/90/h/90 


再说个小时候的傻事。小学二年级，第一次学习书信格式，然后周末布置的作文是“给远方的解放军叔叔写封信”，然后傻乎乎的回家告诉我妈说老师要求给解放军叔叔写信。我妈想了半天只有一个远房亲戚是解放军，于是往老家打着电话要了地址真给写了一封信（那时候打电话还是单位唯一一台的电话），寄出去了。周一老师问我信呢，我说寄出去了，当时老师沉默了很久。后来还收到了那个叔叔的回信。前段时间收拾老房子才看到当年的回信，突然想起来当年那个叔叔收到信的心情该是多么的风中凌乱，而老师的心情该是多么的难以言语啊！

 1949 32

污神社（她是梦）
 100 https://pic.qiushibaike.com/system/avtnew/1857/18570089/thumb/2017121912223219.JPEG?imageView2/1/w/90/h/90 


现在李小璐的事闹得沸沸扬扬，到处都在讨论，我们公司当然也不例外。 837 10

%%竹无心
 23 https://pic.qiushibaike.com/system/avtnew/3586/35861032/thumb/20171218220848.JPEG?imageView2/1/w/90/h/90 


跟老婆看了场恐怖电影，夜场。 1042 9

不帅但很能干的人
 29 https://pic.qiushibaike.com/system/avtnew/931/9318136/thumb/201712241442087.JPEG?imageView2/1/w/90/h/90 


高中晚自习放学后，我们几个男的都住的不远，走路回家，一次，正走着，突然从旁边一大院里窜出了一大狗，冲我们大声吠叫，吓得我们都赶紧跑开！ 1315 11

508先生
 30 https://pic.qiushibaike.com/system/avtnew/2219/22194397/thumb/20141030003016.jpg?imageView2/1/w/90/h/90 


好任性的输入法，背景---太长割---，出差到外地有个乱停车违章，找合作的单位领导帮忙处理，完了发信息“万分感谢”居然弄成“晚饭感谢”，本来200大洋解决的事情硬硬的花了小500，还别说，领导夸咱有“攻官能力”，我勒个去

 181 4

傻晴°
 26 https://pic.qiushibaike.com/system/avtnew/2333/23331917/thumb/2018010811321190.JPEG?imageView2/1/w/90/h/90 


同事出差回来请客，期间有人跟他老婆开玩笑:你这男人出差这么久怕么？看他那样百分之五十会出轨哦！ 1249 10

℡梅心梅肺～
 25 https://pic.qiushibaike.com/system/avtnew/2031/20313229/thumb/20171230153337.JPEG?imageView2/1/w/90/h/90 


拿着钱准备去银行存钱还蚂蚁花呗，儿子看到问我“妈妈，你拿钱干嘛？”我说，我上个月用了蚂蚁花呗的钱，这个月要还啊“儿子说，蚂蚁花的钱干嘛要你还啊？”其实，我也想用了不还的[笑哭]

 1117 9

叶落风吹续
 19 https://pic.qiushibaike.com/system/avtnew/2623/26231676/thumb/2018010810371818.JPEG?imageView2/1/w/90/h/90 


嗯……果然是自己家地里长出来的

 1178 15

吃了两碗又盛
 38 https://pic.qiushibaike.com/system/avtnew/3221/32215536/thumb/201711071252265.JPEG?imageView2/1/w/90/h/90 


媳妇跟她闺蜜去吃火锅，我下班接了儿子，告诉他:你妈去吃火锅了，咱俩还要到店里待一个半小时，晚饭恐怕要糊弄一顿了。 1696 23

米臭百公里
 35 https://pic.qiushibaike.com/system/avtnew/2355/23552011/thumb/20171219214019.JPEG?imageView2/1/w/90/h/90 


看到朋友无精打采，问道：昨天你不是说去洗浴中心放松了吗？该不会被老婆发现了吧？答：老婆倒是没发现，是发现老婆了。

 8594 111

带我去走人生
 28 https://pic.qiushibaike.com/system/avtnew/3536/35369902/thumb/2017112017445568.JPEG?imageView2/1/w/90/h/90 


新群规 2640 64

正月二月
 29 https://pic.qiushibaike.com/system/avtnew/3312/33126063/thumb/20171229214040.JPEG?imageView2/1/w/90/h/90 


姑娘，你男朋友的动鸡变成了冻鸡，拿刀都砍不断。

 972 22

巾帼英雄小木兰
 68 https://pic.qiushibaike.com/system/avtnew/2011/20115333/thumb/20171221191335.JPEG?imageView2/1/w/90/h/90 


想起那时大学毕业不久，家里安排相亲，一看来人，我凑，辅导老师，他见到我也是惊呆了，半晌开口:xx，毕业不去找工作，倒跑来相亲了啊！

 4433 80

你家邻居叫马乐
 34 https://pic.qiushibaike.com/system/avtnew/19/190315/thumb/20151124163156.jpg?imageView2/1/w/90/h/90 


亚当系列故事之二 1687 21

可爱彤文
 30 https://pic.qiushibaike.com/system/avtnew/1632/16320641/thumb/2016090622324829.JPEG?imageView2/1/w/90/h/90 


星期六带俩女儿去买药，结果下楼就让2岁女儿蹲那尿尿，结果她拉粑粑，我就顺手把包放旁边三轮车上从里拿出纸给擦完屁股处理了粑粑，骑上电动车就去买药了，走到药店门口刚要下车发现包没了！立马想到准是忘家里没带出来！赶紧回去拿，走半路想起来是忘到外头三轮车上了！赶紧加速恨不得飞回去拿包，结果我的包还在三轮车上，连拉链都没拉！里面手机现金卡身份证都在！瞬间有种想感谢谁的冲动！

 220 4

老板来碗面汤
 42 https://pic.qiushibaike.com/system/avtnew/1181/11818025/thumb/20140426215733.jpg?imageView2/1/w/90/h/90 


同时两口子都是赌徒，而且每人外债几十万，最近她女儿上大学放寒假，手机换成了爱疯x，我问她多少钱买的，她说，他父母每月给三千生活费都不够花的，哪有钱买手机啊………………，这信息量大了去了啊

 822 19

敷衍、怎么演s
 29 https://pic.qiushibaike.com/system/avtnew/3616/36160314/thumb/2018010422432549.JPEG?imageView2/1/w/90/h/90 


什么意思？？？

 510 221

晓颜诺诺
 27 https://pic.qiushibaike.com/system/avtnew/3435/34350130/thumb/2018010106514149.JPEG?imageView2/1/w/90/h/90 


闺蜜失恋了，陪她去喝酒，越喝越来劲，喝到最后跑大街上去了，边喝边叫：走过路过的朋友们，有钱的捧个钱场呀，小女子要开始献唱了…然后往地上一坐，就开唱了… 950 33

齐恩娅
 26 https://pic.qiushibaike.com/system/avtnew/1910/19101633/thumb/20171114100402.JPEG?imageView2/1/w/90/h/90 


我竟无言以对

 2686 19

未来的宠物医生
 20 https://pic.qiushibaike.com/system/avtnew/1227/12275709/thumb/20160707115041.jpg?imageView2/1/w/90/h/90 


给我表妹买布娃娃她不要，非要作文书，叫她到我家玩，让她看电视玩电脑她也不乐意，嘀嘀咕咕的说自己要回家练习二胡写作业，得了甲沟炎把脚趾甲拔掉在医院修养的时候也没忘记叫她妈妈从家里带几张数学卷子。。。人与人之间的差距真的好大！

 338 6

溜下山的浪小猫
 97 https://pic.qiushibaike.com/system/avtnew/3165/31650411/thumb/2016103016520765.JPEG?imageView2/1/w/90/h/90 


LZ扛水泥的，平时为了省钱，都是在家用冷水冲澡。 2432 40

墨海烟云
 28 https://pic.qiushibaike.com/system/avtnew/2161/21610887/thumb/2018010814345849.JPEG?imageView2/1/w/90/h/90 


在街上遇到了上学时谈的女友，见她身边有个小男孩我说:孩子都这么大了。 1481 10

有图有真相的我
 12 https://pic.qiushibaike.com/system/avtnew/3304/33048009/thumb/20180105160337.JPEG?imageView2/1/w/90/h/90 


一年一度的

 1140 108

茄子家的靓巫婆～
 13 https://pic.qiushibaike.com/system/avtnew/3424/34246786/thumb/20171217181346.JPEG?imageView2/1/w/90/h/90 


吃货儿子上幼儿园那会的趣事。 1080 5

成天日
 33 https://pic.qiushibaike.com/system/avtnew/494/4944719/thumb/20141122233017.jpg?imageView2/1/w/90/h/90 


背景陪母亲住院，母亲手腕上有个住院号3727-----今晚去买烟，听店主跟几个人在讨论码，我以前也尔偶买过几次中过一次200的一般买几块钱，即跟店主说37号27号各买5元，哈哈，九点四十我用手机查了一下竟然开了27，明天给母亲买点好吃的。

 236 11
 
"""



