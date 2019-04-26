# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup


class TianyanchaSpiderSpider(scrapy.Spider):
    name = "tianyancha_spider"
    allowed_domains = []
    script = """
            function main(splash)
                splash.images_enabled = false
                splash:go("%s")
                splash:wait(%s)
                return splash:html()
            end
    """
    start_urls = [
        u'http://www.tianyancha.com/search?key=北京至信普林科技有限公司'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url,
                          self.parse_next_page,
                          meta={
                              'splash': {
                                  'args': {'lua_source': self.script % (url, 5.0)},
                                  'endpoint': 'execute'
                              }
                          })

    def parse_next_page(self, response):
        _soup = BeautifulSoup(response.body, 'html.parser')
        divs = _soup('div', attrs={'class': 'search_right_item'})
        for div in divs[:1]:
            _score = div.find('text', attrs={'x': '27', 'y': '28'})
            score = _score.get_text().strip() if _score else 'unknown'
            enterprise = div.a.get_text().strip() or 'unknown'
            _location = div.find('i', attrs={'class': 'fa fa-map-marker c9'})
            location = _location.next_element.string.strip() if _location else 'unknown'
            print('location: ', location)
            url = div.a['href'] if div.find('a', attrs={'href': True}) else None
            script = """
                    function main(splash)
                        splash.images_enabled = false
                        splash:go("%s")
                        splash:wait(%s)
                        splash:runjs("$('a.ng-binding').click()")
                        splash:wait(%s)
                        return splash:html()
                    end
            """
            if url:
                print('url: %s' % url)
                yield Request(
                    url,
                    self.parse_page,
                    meta={
                        'splash': {
                            'args': {'lua_source': script % (url, 6.0, 1.0)},
                            'endpoint': 'execute'
                        },
                        'score': score,
                        'enterprise': enterprise,
                        'location': location
                    }
                )

    def parse_page(self, response):
        result = {}
        result['enterpirse'] = response.meta.get('enterprise', 'unknown')
        result['score'] = response.meta.get('score', 'unknown')
        result['location'] = response.meta.get('location', 'unknown')
        result['url'] = response.url
        _soup = BeautifulSoup(response.body, 'html.parser')
        div = _soup.find('div', attrs={'class': 'company_info_text'})
        if div:
            result['enterprise_name'] = div.find('div').get_text().strip() if div.find('div') else 'unknown'
            spans = div('span', attrs={'class': 'contact_way_title'})
            for span in spans:
                key = span.get_text().strip()
                if u'网址' in key:
                    continue
                else:
                    value = span.next_element.next_element.strip()
                result[key.strip()[:-1]] = value.strip()
            a = div.find('a', attrs={'ng-if': 'company.websiteList', 'href': True})
            result[u'网址'] = a.get_text().strip() if a else 'unknown'

        # 企业背景
        div = _soup.find('div', attrs={'class': 'baseInfo_model2017'})
        if div:
            ths = [th.get_text().strip() for th in div.table.thead('td') if th.get_text()]
            tds = [td.get_text().strip() if td.get_text() else 'unknown' for td in div.table.tbody('td')]
            for i, th in enumerate(ths):
                result[th] = tds[i]

        # 基本信息
        divs = _soup('div', attrs={'class': 'baseinfo-module-item'})
        for div in divs:
            key = div.find('div', attrs={'class': 'baseinfo-module-content-title'})
            value = div.find('div', attrs={'class': 'baseinfo-module-content-value'})
            result[key.get_text().strip()] = value.get_text().strip().split()[0] if value else 'unknown'
        div = _soup.find('div', attrs={'class': 'company-content'})
        if div:
            table = div.find('table')
            if table:
                tds = table('td', attrs={'class': 'basic-td'})
                for td in tds:
                    key_value = td.get_text().strip().split(u'：') if td else None
                    if key_value:
                        # print(key_value)
                        result[key_value[0].strip()] = ''.join(key_value[1:])
                    else:
                        print('have no key_value')
            else:
                print('have no table')
        else:
            print('have no div row b-c-white company-content')

        # 主要人员
        divs = _soup('div', attrs={'class': 'staffinfo-module-content'})
        name_postion = []
        for div in divs:
            _dict = {}
            key = div.find('div', attrs={'class': 'staffinfo-module-content-title'})
            _dict[u'name'] = key.get_text().strip() if key else 'unknown'
            value = div.find('div', attrs={'class': 'staffinfo-module-content-value'})
            _dict[u'postion'] = value.get_text().strip().split()[0] if value else 'unknown'
            name_postion.append(_dict)
        result['name_postion'] = name_postion
        result['is_down'] = True

        # 对外投资
        div = _soup.find('div', attrs={'class': 'out-investment-container ng-scope'})
        if div:
            table = div.find('table', attrs={'class': 'table companyInfo-table'})
            if table:
                trs = table('tr')
                ths = [th.get_text().strip() for th in trs[0]('th') if th.get_text()]
                investment = []
                for tr in trs[1:]:
                    tds = [td.get_text().strip() if td.get_text() else None for td in tr('td')]
                    investment.append(dict(zip(ths, tds)))
                result['investment'] = investment

        # 融资历史
        div = _soup.find('div', attrs={'ng-if': 'dataItemCount.companyRongzi>0'})
        if div:
            table = div.find('table', attrs={'class': 'table companyInfo-table'})
            if table:
                trs = table('tr')
                ths = [th.get_text().strip() for th in trs[0]('th') if th.get_text()]
                rongzi = []
                for tr in trs[1:]:
                    tds = [td.get_text().strip() if td.get_text() else None for td in tr('td')]
                    rongzi.append(dict(zip(ths, tds)))
                result['rongzi'] = rongzi
            else:
                result['rongzi'] = []
        else:
            result['rongzi'] = []
        yield result
