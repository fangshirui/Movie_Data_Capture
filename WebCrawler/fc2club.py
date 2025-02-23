import sys
sys.path.append('../')
from lxml import etree#need install
import json
import ADC_function

def getTitle_fc2com(htmlcode): #获取标题
    html = etree.fromstring(htmlcode,etree.HTMLParser())
    result = str(html.xpath('//*[@class="show-top-grids"]/div[1]/h3/text()')).strip(" ['']")
    return result
def getActor_fc2com(htmlcode):
    try:
        html = etree.fromstring(htmlcode, etree.HTMLParser())
        result = str(html.xpath('//*[@class="show-top-grids"]/div[1]/h5[5]/a/text()')).strip(" ['']")
        return result
    except:
        return ''
def getStudio_fc2com(htmlcode): #获取厂商
    try:
        html = etree.fromstring(htmlcode, etree.HTMLParser())
        result = str(html.xpath('//*[@class="show-top-grids"]/div[1]/h5[3]/a[1]/text()')).strip(" ['']")
        return result
    except:
        return ''
def getNum_fc2com(htmlcode):     #获取番号
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    title = str(html.xpath('//*[@class="show-top-grids"]/div[1]/h3/text()')).strip(" ['']")
    num = title.split(' ')[0]
    if num.startswith('FC2') != True:
        num = ''
    return num
def getRelease_fc2com(htmlcode2): #
    return ''
def getCover_fc2com(htmlcode2): #获取img #
    html = etree.fromstring(htmlcode2, etree.HTMLParser())
    imgUrl = str(html.xpath('//*[@class="slides"]/li[1]/img/@src')).strip(" ['']")
    imgUrl = imgUrl.replace('../','https://fc2club.net/')
    return imgUrl
def getTag_fc2com(htmlcode):     #获取tag
    html = etree.fromstring(htmlcode,etree.HTMLParser())
    a = html.xpath('//*[@class="show-top-grids"]/div[1]/h5[4]/a')
    tag = []
    for i in range(len(a)):
        tag.append(str(a[i].xpath('text()')).strip("['']"))
    return tag
def getYear_fc2com(release):
        return ''

def getExtrafanart(htmlcode):  # 获取剧照
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    imgUrl = str(html.xpath('//*[@class="slides"]/li[1]/img/@src')).strip(" ['']")
    imgUrl = imgUrl.replace('../','https://fc2club.net/')
    return imgUrl

def getTrailer(htmlcode):
    return ''

def main(number):
    try:
        number = number.replace('FC2-', '').replace('fc2-', '')
        webUrl = 'https://fc2club.net/html/FC2-' + number + '.html'
        htmlcode2 = ADC_function.get_html(webUrl)
        actor = getActor_fc2com(htmlcode2)
        if getActor_fc2com(htmlcode2) == '':
            actor = 'FC2系列'
        dic = {
            'title': getTitle_fc2com(htmlcode2),
            'studio': getStudio_fc2com(htmlcode2),
            'year': getYear_fc2com(getRelease_fc2com(htmlcode2)),
            'outline': '',  # getOutline_fc2com(htmlcode2),
            'runtime': '',
            'director': getStudio_fc2com(htmlcode2),
            'actor': actor,
            'release': getRelease_fc2com(htmlcode2),
            'number': 'FC2-' + number,
            'label': '',
            'cover': getCover_fc2com(htmlcode2),
            'extrafanart': getExtrafanart(htmlcode2),
            "trailer": getTrailer(htmlcode2),
            'imagecut': 0,
            'tag': getTag_fc2com(htmlcode2),
            'actor_photo': '',
            'website': 'https://fc2club.net/html/FC2-' + number + '.html/',
            'source': 'https://fc2club.net/html/FC2-' + number + '.html/',
            'series': '',
        }
    except Exception as e:
        if ADC_function.config.getInstance().debug():
            print(e)
        dic = {"title": ""}
    js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js

if __name__ == '__main__':
    print(main('FC2-402422'))

