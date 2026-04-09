from __future__ import annotations


class MockLLMClient:
    def generate_json(self, prompt: str) -> dict:
        prompt_lower = prompt.lower()

        if "number of islands" in prompt_lower or "grid" in prompt_lower:
            return {
                "problem_summary": "Count how many connected land components exist in the grid.",
                "recommended_patterns": ["DFS", "BFS", "Graph Traversal"],
                "pattern_reason": "The grid behaves like a graph where adjacent land cells form connected components.",
                "brute_force_approach": "Try expanding from each land cell repeatedly without a shared visited strategy, then deduplicate counts.",
                "optimal_approach": "Scan the grid once and launch DFS or BFS whenever you find an unvisited land cell, marking the full island before continuing.",
                "time_complexity": "O(m * n)",
                "space_complexity": "O(m * n)",
                "hint_sequence": [
                    "Think about what it means for two land cells to belong to the same island.",
                    "What should happen when you discover a land cell that has not been visited yet?",
                    "Use a traversal to mark the entire connected component before moving on.",
                ],
                "follow_up_questions": [
                    "How would you solve it if diagonal cells also counted as connected?",
                    "What changes if you are not allowed to mutate the input grid?",
                    "How would you avoid recursion depth issues on very large grids?",
                ],
                "common_mistakes": [
                    "Forgetting to mark visited cells.",
                    "Counting each land cell instead of each island.",
                    "Missing boundary checks when exploring neighbors.",
                ],
            }

        if "two numbers" in prompt_lower or "target" in prompt_lower:
            return {
                "problem_summary": "Find the pair of indices whose values add up to the target.",
                "recommended_patterns": ["Hash Map"],
                "pattern_reason": "The problem becomes efficient once you can look up a needed complement in constant time while scanning once.",
                "brute_force_approach": "Check every pair of indices and test whether the two values sum to the target.",
                "optimal_approach": "Track previously seen values in a hash map so each new number can immediately check whether its complement was seen earlier.",
                "time_complexity": "O(n)",
                "space_complexity": "O(n)",
                "hint_sequence": [
                    "Start with the simplest way to test all possible pairs.",
                    "Ask what information would let you avoid rechecking earlier numbers.",
                    "A map from value to index lets you find the missing complement in constant time.",
                ],
                "follow_up_questions": [
                    "How would the solution change if the array were sorted?",
                    "What if the problem asked for values instead of indices?",
                    "How would you handle multiple valid pairs?",
                ],
                "common_mistakes": [
                    "Using the same element twice.",
                    "Returning values instead of indices.",
                    "Overwriting duplicate values without thinking through the effect on indices.",
                ],
            }

        return {
            "problem_summary": "Restate the problem in clear interview terms before choosing a solution pattern.",
            "recommended_patterns": ["Array", "Hash Map"],
            "pattern_reason": "This mock response defaults to common interview patterns when the problem shape is ambiguous.",
            "brute_force_approach": "Begin with the most direct solution that checks all relevant candidates.",
            "optimal_approach": "Look for repeated work and replace it with a data structure or traversal strategy that avoids recomputation.",
            "time_complexity": "O(n^2)",
            "space_complexity": "O(n)",
            "hint_sequence": [
                "What is the most direct correct solution?",
                "Where is repeated work happening?",
                "Which data structure would make the repeated operation faster?",
            ],
            "follow_up_questions": [
                "What input constraints would change your approach?",
                "How would you explain the tradeoffs in an interview?",
                "What edge cases would you test first?",
            ],
            "common_mistakes": [
                "Optimizing before proving the brute-force idea works.",
                "Ignoring edge cases until the end.",
                "Stating complexity without justifying it.",
            ],
        }