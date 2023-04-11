class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        left = 0
        right = 0
        count = 0
        players.sort()
        trainers.sort()
        while left < len(players) and right < len(trainers):
            while left < len(players) and right < len(trainers) and players[left] <= trainers[right]:
                count += 1
                left += 1
                right += 1
            right += 1
        return count
