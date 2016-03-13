angular.module 'starthack'
  .service 'MenuStates', ->
    ENTRY: 0,
    MODE_SELECTION: 1,
    RANKING: 2,
    EXIT: 3


angular.module 'starthack'
  .controller 'MenuController', ($scope, MenuStates) ->
    $scope.menuStates = MenuStates
    $scope.state = MenuStates.ENTRY

    $scope.main = -> $scope.state = MenuStates.ENTRY

    $scope.play = (gameType) ->
      if not gameType
        $scope.state = MenuStates.MODE_SELECTION
        return

      $state.go 'game'
