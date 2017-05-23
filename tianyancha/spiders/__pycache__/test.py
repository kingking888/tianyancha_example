
# coding:utf8
import unittest
from bs4 import BeautifulSoup


class TianYanChaTest(unittest.TestCase):
    
    def setUp(self):
        self.soup = BeautifulSoup(open('./page_source.html'), 'html.parser')

    def tearDown(self):
        pass

    def test_parse_page(self):
        result = {}
        div = self.soup.find('div', attrs={'class': 'company_info_text'})
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
        divs = self.soup('div', attrs={'ng-click': 'goToPage(temp)'})
        for div in divs:
            key_value = div.get_text().strip().split()
            if len(key_value) >= 2:
                result[key_value[0].strip()] = key_value[1].strip()

        # 基本信息
        divs = self.soup('div', attrs={'class': 'baseinfo-module-item'})
        for div in divs:
            key = div.find('div', attrs={'class': 'baseinfo-module-content-title'})
            value = div.find('div', attrs={'class': 'baseinfo-module-content-value'})
            result[key.get_text().strip()] = value.get_text().strip().split()[0] if value else 'unknown'

        # 主要人员
        divs = self.soup('div', attrs={'class': 'staffinfo-module-content'})
        name_postion = []
        for div in divs:
            _dict = {}
            key = div.find('div', attrs={'class': 'staffinfo-module-content-title'})
            _dict[u'name'] = key.get_text().strip() if key else 'unknown'
            value = div.find('div', attrs={'class': 'staffinfo-module-content-value'})
            _dict[u'postion'] = value.get_text().strip().split()[0] if value else 'unknown'
            name_postion.append(_dict)
        result['name_postion'] = name_postion

        # 对外投资
        div = self.soup.find('div', attrs={'class': 'out-investment-container ng-scope'})
        table = div.find('table', attrs={'class': 'table companyInfo-table'})
        trs = table('tr')
        ths = [th.get_text().strip() for th in trs[0]('th') if th.get_text()]
        investment = []
        for tr in trs[1:]:
            tds = [td.get_text().strip() if td.get_text() else None for td in tr('td')]
            investment.append(dict(zip(ths, tds)))
        result['investment'] = investment

        # for key, value in result.items():
        #     print(key.encode('utf8'))
        #     if isinstance(value, basestring):
        #         print(value.encode('utf8'))
        #     else:
        #         print(value)


if __name__ == '__main__':
    unittest.main()