from random import randint
from city import BuildingType

class Optimizer:
    def __init__(self, city):
        """An optimizer that iteratively optimizes a given city grid."""
        self._city = city
        self._skyscraper_optimized = False  # Flag to track skyscraper optimization status
        self._office_optimized = False  # Flag to track office optimization status

    def count_adjacent_skyscrapers(self, row, col):
        """Counts the number of skyscrapers adjacent to a given position (including diagonals)."""
        adjacent_positions = [
            (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),
            (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)
        ]
        count = 0
        for r, c in adjacent_positions:
            if 0 <= r < self._city.rows and 0 <= c < self._city.cols:
                if self._city.get_building_type(r, c) == BuildingType.SKYSCRAPER:
                    count += 1
        return count

    def calculate_score(self):
        """Calculates the total score based on the number of adjacent skyscrapers and bad office placements."""
        total_score = 0
        for row in range(self._city.rows):
            for col in range(self._city.cols):
                if self._city.get_building_type(row, col) == BuildingType.SKYSCRAPER:
                    total_score += self.count_adjacent_skyscrapers(row, col)

                    # Penalize if there is no office adjacent to the skyscraper
                    office_nearby = False
                    adjacent_positions = [
                        (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),
                        (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)
                    ]
                    for r, c in adjacent_positions:
                        if 0 <= r < self._city.rows and 0 <= c < self._city.cols:
                            if self._city.get_building_type(r, c) == BuildingType.OFFICE:
                                office_nearby = True
                                break
                    if not office_nearby:
                        total_score += 1

        return total_score

    def swap_offices(self):
        """Swaps offices with random non-office, non-skyscraper, non-high-rise tiles."""
        for row in range(self._city.rows):
            for col in range(self._city.cols):
                if self._city.get_building_type(row, col) == BuildingType.OFFICE:
                    for _ in range(5):  # Try swapping with 5 random non-office, non-skyscraper, non-high-rise buildings
                        row2, col2 = randint(0, self._city.rows - 1), randint(0, self._city.cols - 1)
                        if (
                            self._city.get_building_type(row2, col2) not in
                            [BuildingType.OFFICE, BuildingType.SKYSCRAPER, BuildingType.HIGHRISE]
                        ):
                            # Swap office with a random non-office, non-skyscraper, non-high-rise building
                            self._city.swap_buildings(row, col, row2, col2)
                            break  # Exit the loop after a successful swap

    def skyscraper_optimization_step(self):
        """Optimizes skyscrapers until the score is 0."""
        best_score = self.calculate_score()

        for row1 in range(self._city.rows):
            for col1 in range(self._city.cols):
                if self._city.get_building_type(row1, col1) == BuildingType.SKYSCRAPER:
                    for _ in range(5):  # Try swapping with 5 random non-skyscraper buildings
                        row2, col2 = randint(0, self._city.rows - 1), randint(0, self._city.cols - 1)
                        if self._city.get_building_type(row2, col2) != BuildingType.SKYSCRAPER:
                            # Swap skyscraper with a random non-skyscraper building
                            self._city.swap_buildings(row1, col1, row2, col2)

                            # Calculate new score
                            new_score = self.calculate_score()

                            # If the new score is better or the office swap resulted in a lower score, keep the swap
                            if new_score < best_score or self.calculate_score() < best_score:
                                best_score = new_score
                            else:
                                self._city.swap_buildings(row1, col1, row2, col2)
                            break  # Exit the loop after a successful swap

        # Stop swapping skyscrapers if the score is 0
        if best_score == 0:
            self._skyscraper_optimized = True

    def step(self, print_info=False):
        """Performs a single optimization step."""
        
        if not self._skyscraper_optimized:
            # Optimize skyscrapers until the score is 0
            self.skyscraper_optimization_step()
            return True  # Continue skyscraper optimization

        if not self._office_optimized:
            # Skyscraper optimization is complete, now optimize offices
            self.swap_offices()

            # Check if every skyscraper/high-rise has an office nearby
            for row in range(self._city.rows):
                for col in range(self._city.cols):
                    if self._city.get_building_type(row, col) in [BuildingType.SKYSCRAPER, BuildingType.HIGHRISE]:
                        office_nearby = False
                        adjacent_positions = [
                            (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),
                            (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)
                        ]
                        for r, c in adjacent_positions:
                            if 0 <= r < self._city.rows and 0 <= c < self._city.cols:
                                if self._city.get_building_type(r, c) == BuildingType.OFFICE:
                                    office_nearby = True
                                    break
                        if not office_nearby:
                            return True  # Continue office optimization

            self._office_optimized = True  # Stop swapping offices once optimized

        if print_info:
            print("New score:", self.calculate_score())
            print("New city layout:")
            self._city.print_plots()

        return False  # Stop optimization

    def optimize(self, print_info=True):
        """
        Runs the optimizer until the score reaches 0 or no further improvement, or after 50 iterations.
        Args:
            print_info (bool):
                Whether to print information about the optimization step.
        """
        optimization_count = 0  # Add a counter to prevent an infinite loop
        while optimization_count < 50 and self.step(print_info):
            optimization_count += 1
            print(f"Optimization step {optimization_count}")

        if self.calculate_score() == 0:
            print("Optimization complete. Final score:", self.calculate_score())
            print("0 bad neighbors!")
        else:
            print("Optimization complete. Final score:", self.calculate_score())
