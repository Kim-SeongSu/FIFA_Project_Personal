# TCC(Team color crawling) main
## module import
import data_io
import TCL_crawling
import TCD_crawling


## run
# teamcolor_types = TCL_crawling.Team_color_list()
### teamcolor list 데이터 로드 : 새로 팀컬러 목록을 크롤링 하지 않고 기존의 저장된 목록을 불러올 때 사용!!
teamcolor_type = data_io.load_TCL_data()

df_teamcolor_club,df_teamcolor_nation,df_teamcolor_reinforce,df_teamcolor_relation,df_teamcolor_special = TCD_crawling.team_color_detail(teamcolor_type)
### teamcolor detail 데이터 로드
# df_teamcolor_club,df_teamcolor_nation,df_teamcolor_reinforce,df_teamcolor_relation,df_teamcolor_special = data_io.load_TCL_data()