/**
 * Problem 1: Two Sum
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * 
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums: number[], target: number): number[] {
    const seen = new Map<number, number>();
    
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (seen.has(complement)) {
            return [seen.get(complement)!, i];
        }
        seen.set(nums[i], i);
    }
    
    return [];
}

// Inline test assertions
console.assert(JSON.stringify(twoSum([2, 7, 11, 15], 9)) === JSON.stringify([0, 1]), "Test 1 Failed");
console.assert(JSON.stringify(twoSum([3, 2, 4], 6)) === JSON.stringify([1, 2]), "Test 2 Failed");
console.assert(JSON.stringify(twoSum([3, 3], 6)) === JSON.stringify([0, 1]), "Test 3 Failed");
console.log("All TypeScript test cases for Problem 1 (Two Sum) passed!");
