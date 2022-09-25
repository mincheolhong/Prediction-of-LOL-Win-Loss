# Prediction-of-LOL-Win-Loss
> **롤** 승률 예측 프로그램을 사용해본 경험이 있는데 해당 승률에 부정확하다고 생각했다. 
그리고 본인은 롤 골드 티어 구간에서 오래 머물다 게임을 이기는 원리를 깨닫고 플레티넘으로 성장한 경험이 있는데
이런 성장에 가장 큰 영향이 게임 시작 전에 팀원, 상대, 본인의 데이터를 분석해 이를 활용하여 플레이한 전략이 유효했다.
이러한 경험으로 해당 도메인(롤 골드 티어 구간)에대해 어느정도 잘 이해하고 있다고 생각해서 이를 머신러닝에 잘 활용할 수 있다는 생각을 했다.
#### 롤 골드 구간에서 승패를 예측해보자 !!

# 데이터 수집
* 어떻게 수집할까?   
  * op.gg 롤 전적 검색 사이트
  * Riot api
- 얼마나 수집할까?
  - 일단 만 개를 목표로 수집해보자.
- 어떤 데이터를 수집할까?
  - 1게임 단위로 플레이어들의 실력의 지표가 되는 데이터들을 수집하자
    - 골드, 경험치, cs, kda 등등의 최근 10경기 데이터
    
# Riot API
다음의 탭들에서 해당 정보를 가져올 수 있는 api가 있다

 * SUMMONER-V4
   * Get a summoner by summoner name
 * LEAGUE-V4
   * Get all the league entries
 * MATCH-V5
   * Get a list of match ids by puuid
   * Get a match by match id
   * Get a match timeline by match id
 * SPECTATOR-V4
   * Get current game information for the given summoner ID
   * Get list of featured games
