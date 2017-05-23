# encoding:utf8
import unittest
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class TianYanChaTest(unittest.TestCase):
    
    def setUp(self):
        self.response = HtmlResponse(url='123', body=open('./page_source.html').read())

    def tearDown(self):
        pass

    @unittest.skip("demonstrating skipping")
    def test_parse_page(self):
        phone = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/span[1]/text()').extract()[-1] or 'unknown'
        mail = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/span[2]/text()').extract()[-1] or 'unknown'
        website = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/span[3]/a/text()').extract_first(default='unknown')
        address = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/span[4]/text()').extract()[-1] or 'unknown'
        # summary = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div').extract()

        main_staff_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[3]/span/text()').extract_first(default='unknown')
        shareholder_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[4]/span/text()').extract_first(default='unknown')
        inverst_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[5]/span/text()').extract_first(default='unknown')
        modify_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[3]/div[1]/span/text()').extract_first(default='unknown')
        report_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/span/text()').extract_first(default='unknown')
        branch_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[3]/div[3]/span/text()').extract_first(default='unknown')
        
        finance_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div[1]/span/text()').extract_first(default='unknown')
        team_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/span/text()').extract_first(default='unknown')
        business_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/span/text()').extract_first(default='unknown')
        invest_event_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div[4]/span/text()').extract_first(default='unknown')
        competing_products_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div[5]/span/text()').extract_first(default='unknown')
        
        lawsuit_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[3]/div[2]/div[1]/span/text()').extract_first(default='unknown')
        legal_notice_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[3]/div[2]/div[2]/span/text()').extract_first(default='unknown')
        dishonesty_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[3]/div[2]/div[3]/span/text()').extract_first(default='unknown')
        being_executed_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[3]/div[2]/div[4]/span/text()').extract_first(default='unknown')
        
        business_abnormal_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[4]/div[2]/div[1]/span/text()').extract_first(default='unknown')
        penalties_administra_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[4]/div[2]/div[2]/span/text()').extract_first(default='unknown')
        be_illegal_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[4]/div[2]/div[3]/span/text()').extract_first(default='unknown')
        equity_is_pledged_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[4]/div[2]/div[4]/span/text()').extract_first(default='unknown')
        chattel_mortgage_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[4]/div[2]/div[5]/span/text()').extract_first(default='unknown')
        tax_arrears_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[4]/div[3]/div/span/text()').extract_first(default='unknown')
        
        tender_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[2]/div[1]/span/text()').extract_first(default='unknown')
        bonds_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[2]/div[2]/span/text()').extract_first(default='unknown')
        purchase_land_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[2]/div[3]/span/text()').extract_first(default='unknown')
        recruitment_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[2]/div[4]/span/text()').extract_first(default='unknown')
        tax_rating_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[2]/div[5]/span/text()').extract_first(default='unknown')
        check_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[3]/div[1]/span/text()').extract_first(default='unknown')
        product_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[3]/div[2]/span/text()').extract_first(default='unknown')
        certifications_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[3]/div[3]/span/text()').extract_first(default='unknown')
        
        trademark_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[6]/div[2]/div[1]/span/text()').extract_first(default='unknown')
        patent_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[6]/div[2]/div[2]/span/text()').extract_first(default='unknown')
        copyright_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[6]/div[2]/div[3]/span/text()').extract_first(default='unknown')
        website_record_num = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[6]/div[2]/div[4]/span/text()').extract_first(default='unknown')

        represent = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[5]/div[1]/div/div[2]/div[2]/a[1]/text()').extract_first(default='unknown')
        capital = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[5]/div[2]/div/div[2]/div[2]/text()').extract_first(default='unknown')
        regdate = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[5]/div[3]/div/div[2]/div[2]/text()').extract_first(default='unknown')
        status = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[5]/div[4]/div/div[2]/div[2]/text()').extract_first(default='unknown')
        business_scope = self.response.xpath('//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div/div[6]/table/tbody/tr[6]/td/div/span/span/text()').extract_first(default='unknown')
        
        person = []
        divs = self.response.xpath('//div[@class="staffinfo-module-content"]')
        for div in divs:
            _dict = {}
            name = div.xpath('div[@class="staffinfo-module-content-title"]/a/text()').extract_first(default='unknown')
            values = div.xpath('div[@class="staffinfo-module-content-value"]/span/text()').extract()
            value = ''.join(values) or 'unknown'
            _dict['name'] = name.strip()
            _dict['value'] = value.strip()
            person.append(_dict)

        divs = self.response.xpath('//div[@class="out-investment-container ng-scope"]')
        tables = divs[0].xpath('div/table[@class="table companyInfo-table"]')
        ths = tables[0].xpath('thead/tr/th/text()').extract()
        trs = tables[0].xpath('tbody/tr')
        invests = []
        for tr in trs:
            _tds = tr.xpath('td')
            tds = []
            for i, td in enumerate(_tds):
                if i == 0:
                    td=td.xpath('a/span/text()').extract_first(default='unknown') or None
                    tds.append(td)
                else:
                    t = td.xpath('span/text()').extract_first(default='unknown') or None
                    tds.append(t)
            invests.append(dict(zip(ths, tds)))

    def test_href(self):
        pass
        # self.response
        # _soup = BeautifulSoup(response.body, 'html.parser')
        # divs = _soup('div', attrs={'class': 'search_right_item'})
        # for div in divs:
        #     url = div.a['href'] if div.find('a', attrs={'href': True}) else None

        # for key, value in locals().items():
        #     print(key.encode('utf8'))
        #     if isinstance(value, basestring):
        #         print(value.encode('utf8'))
        #     else:
        #         print(value)
        # result = {}
        # div = self.soup.find('div', attrs={'class': 'company_info_text'})
        # if div:
        #     result['enterprise_name'] = div.find('div').get_text().strip() if div.find('div') else 'unknown'
        #     spans = div('span', attrs={'class': 'contact_way_title'})
        #     for span in spans:
        #         key = span.get_text().strip()
        #         if u'网址' in key:
        #             continue
        #         else:
        #             value = span.next_element.next_element.strip()
        #         result[key.strip()[:-1]] = value.strip()
        #     a = div.find('a', attrs={'ng-if': 'company.websiteList', 'href': True})
        #     result[u'网址'] = a.get_text().strip() if a else 'unknown'

        # # 企业背景
        # divs = self.soup('div', attrs={'ng-click': 'goToPage(temp)'})
        # for div in divs:
        #     key_value = div.get_text().strip().split()
        #     if len(key_value) >= 2:
        #         result[key_value[0].strip()] = key_value[1].strip()

        # # 基本信息
        # divs = self.soup('div', attrs={'class': 'baseinfo-module-item'})
        # for div in divs:
        #     key = div.find('div', attrs={'class': 'baseinfo-module-content-title'})
        #     value = div.find('div', attrs={'class': 'baseinfo-module-content-value'})
        #     result[key.get_text().strip()] = value.get_text().strip().split()[0] if value else 'unknown'

        # # 主要人员
        # divs = self.soup('div', attrs={'class': 'staffinfo-module-content'})
        # name_postion = []
        # for div in divs:
        #     _dict = {}
        #     key = div.find('div', attrs={'class': 'staffinfo-module-content-title'})
        #     _dict[u'name'] = key.get_text().strip() if key else 'unknown'
        #     value = div.find('div', attrs={'class': 'staffinfo-module-content-value'})
        #     _dict[u'postion'] = value.get_text().strip().split()[0] if value else 'unknown'
        #     name_postion.append(_dict)
        # result['name_postion'] = name_postion

        # # 对外投资
        # div = self.soup.find('div', attrs={'class': 'out-investment-container ng-scope'})
        # table = div.find('table', attrs={'class': 'table companyInfo-table'})
        # trs = table('tr')
        # ths = [th.get_text().strip() for th in trs[0]('th') if th.get_text()]
        # investment = []
        # for tr in trs[1:]:
        #     tds = [td.get_text().strip() if td.get_text() else None for td in tr('td')]
        #     investment.append(dict(zip(ths, tds)))
        # result['investment'] = investment

        # for key, value in result.items():
        #     print(key.encode('utf8'))
        #     if isinstance(value, basestring):
        #         print(value.encode('utf8'))
        #     else:
        #         print(value)


if __name__ == '__main__':
    unittest.main()