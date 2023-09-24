class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * (glass_per_row + 1) for glass_per_row in range(query_row + 1)]
        tower[0][0] = poured

        for row in range(query_row):
            for glass in range(row + 1):
                quantity = (tower[row][glass] - 1) / 2
                tower[row + 1][glass] += max(quantity, 0)
                tower[row + 1][glass + 1] += max(quantity, 0)

        return min(1, tower[query_row][query_glass])
