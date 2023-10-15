package io.github.mariazevedo88.hc.prepkit.stacks;

import java.util.ArrayDeque;
import java.util.Deque;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * There are a number of plants in a garden. Each of these plants has been treated with some amount of pesticide. 
 * After each day, if any plant has more pesticide than the plant on its left, being weaker than the left one, 
 * it dies.
 * 
 * You are given the initial values of the pesticide in each of the plants. Print the number of days after which 
 * no plant dies, i.e. the time after which there are no plants with more pesticide content than the plant to their 
 * left.
 * 
 * For example, pesticide levels p=[3,6,2,7,5]. Using a 1-indexed array, day 1 plants 2 and 4 die leaving p=[3,2,5]. 
 * On day 2, plant 3 of the current array dies leaving p=[3,2]. As there is no plant with a higher concentration of 
 * pesticide than the one to its left, plants stop dying after day 2.
 * 
 * Function Description
 * 
 * Complete the function poisonousPlants in the editor below. It must return an integer representing the number of 
 * days until plants no longer die from pesticide.
 * 
 * poisonousPlants has the following parameter(s):
 * 
 * - p: an array of integers representing pesticide levels in each plant
 * 
 * Input Format
 * 
 * The first line contains an integer n, the size of the array p.
 * The next line contains n space-separated integers p[i].
 * 
 * Constraints
 * 
 * 1 <= n <= 10^5
 * 0 <= p[i] <= 10^9
 * 
 * Output Format
 * 
 * Output an integer equal to the number of days after which no plants die.
 * 
 * Sample Input
 * 
 * 7
 * 6 5 8 4 7 10 9
 * 
 * Sample Output
 * 
 * 2
 * 
 * Explanation
 * 
 * Initially all plants are alive.
 * Plants = {(6,1), (5,2), (8,3), (4,4), (7,5), (10,6), (9,7)}
 * Plants[k] = (i,j) => jth plant has pesticide amount = i.
 * After the 1st day, 4 plants remain as plants 3, 5, and 6 die.
 * Plants = {(6,1), (5,2), (4,4), (9,7)}
 * After the 2nd day, 3 plants survive as plant 7 dies.
 * Plants = {(6,1), (5,2), (4,4)}
 * After the 2nd day the plants stop dying.
 * 
 * @author Mariana Azevedo
 * @since 08/05/2020
 */
public class PoisonousPlants {
	
	private static final Logger logger = LoggerFactory.getLogger(PoisonousPlants.class);

	public static void main(String[] args) {
		
		int[] pesticides1 = {6,5,8,4,7,10,9};
		logger.info(String.valueOf(poisonousPlants(pesticides1)));
		
		int[] pesticides2 = {3,2,5,4};
		logger.info(String.valueOf(poisonousPlants(pesticides2)));
		
		int[] pesticides3 = {4,3,7,5,6,4,2};
		logger.info(String.valueOf(poisonousPlants(pesticides3)));
	}
	
	// Complete the poisonousPlants function below.
    static int poisonousPlants(int[] p) {

        int[] days = new int[p.length];
        int minDays = p[0];
        int maxDays = 0;
        Deque<Integer> stack = new ArrayDeque<>();

        stack.push(0);

        for (int i = 1; i < p.length; i++){
            
        	if (p[i] > p[i - 1]) {
            	days[i] = 1;
            }

            minDays = minDays < p[i] ? minDays : p[i];

            while (!stack.isEmpty() && p[stack.peek()] >= p[i]){
                
            	increaseNumberOfDays(p, days, minDays, stack, i);
                stack.pop();
            }

            maxDays = maxDays > days[i] ? maxDays : days[i];
            stack.push(i);
        }
        
        return maxDays;
    }

	private static void increaseNumberOfDays(int[] p, int[] days, int minDays, Deque<Integer> stack, int i) {
		if (p[i] > minDays) {
			days[i] = days[i] > days[stack.peek()] + 1 ? 
					days[i] : days[stack.peek()] + 1;
		}
	}

}
