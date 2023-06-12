import pandas as pd
import crawler

if __name__ == '__main__':
    CWE_List = pd.DataFrame(columns=['ID', 'NAME', 'DESCRIPTION','TYPE','PHASE','C_CODE_EXAMPLE'])

    for ID in range(1,1396):
        new_CWE = {}
        new_CWE['ID'] = ID
        print(ID)

        soup = crawler.get_html_soup(ID)
        new_CWE['NAME'] = crawler.parse_name(soup)
        new_CWE['DESCRIPTION'] = crawler.parse_desc(soup)
        new_CWE['TYPE'] = crawler.parse_type(soup)
        new_CWE['PHASE'] = crawler.parse_phase(soup)
        new_CWE['C_CODE_EXAMPLE'] = crawler.has_c_code_example(soup)

        new_row = pd.Series(new_CWE)
        CWE_List = pd.concat([CWE_List, new_row.to_frame().T], ignore_index = True)

    CWE_List.set_index('ID',inplace=True)
    CWE_List.to_excel("CWE list.xlsx") 