from bs4 import BeautifulSoup
import re
import urllib.request

team_list = []
points_list = []


def create_ranking(team_tables_td, clr_points_table):
    for td in team_tables_td:
        if td.a.string in team_list:
            index_team_list = team_list.index(td.a.string)
            index_team_tables = team_tables_td.index(td)
            points_list[index_team_list] = str(int(points_list[index_team_list]) + int(clr_points_table[index_team_tables]))
        else:
            index_team_tables = team_tables_td.index(td)
            team_list.append(td.a.string)
            points_list.append(clr_points_table[index_team_tables])


def clear_points_table(points_tables_td):
    tmp_points_list = []
    for b in points_tables_td:
        isMatchingObj = re.search(r"\d+", b.string)
        if isMatchingObj is not None:
            tmp_points_list.append(b.string)
    return tmp_points_list

def merge_lists(team_list, points_list):
    merged_list = []
    for i in range(len(team_list)):
        merged_list.append(team_list[i] + ": " + points_list[i] + "\n")
    merged_list.sort(key= lambda x: int(re.search(r'\d+$', x).group()), reverse=True)
    return merged_list


for i in range(2008,2019):
    response = urllib.request.urlopen("https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_({}/{})".format(i, i+1))
    soup = BeautifulSoup(response, "html.parser")
    tables = soup.find_all("table", {"class" : "wikitable"})
    if (i <= 2012):
        case_nr = 1
    else:
        case_nr = 2

    team_tables_td = tables[case_nr].find_all("td", {"align": "left"})
    points_tables_td = tables[case_nr].find_all("b")

    clr_points_table = clear_points_table(points_tables_td)
    create_ranking(team_tables_td, clr_points_table)

if (len(team_list) == len(points_list)):
    ranking = merge_lists(team_list, points_list)
    j = 1
    for position in ranking:
        print("{}. {}".format(j, position))
        j += 1