#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>
#include <limits.h>

void print1DIntArray(int* arr, int arrSize){
    printf("[");
    for(int i = 0; i < arrSize; i++){
        if(i + 1 >= arrSize){
            printf("%d]\n", arr[i]);
        } else {
            printf("%d, ", arr[i]);
        }
    }
}

// --- 1071. Greatest Common Divisor of Strings ---
char* gcdOfStrings(char* str1, char* str2){

    // Get string lengths
    int n1 = strlen(str1);
    int n2 = strlen(str2);

    char* base;
    int baseLen;

    // Find the BASE
    if(n1  < n2){
        baseLen = n1;
        base = malloc((baseLen + 1) * sizeof(char));
        strcpy(base, str1);
    } else {
        baseLen = n2;
        base = malloc((baseLen + 1) * sizeof(char));
        strcpy(base, str2);
    }

    for(int i = baseLen - 1; i >= 0; i--){
        
        // Check if divisible
        if(n1 % baseLen == 0 && n2 % baseLen == 0 && baseLen > 0){

            int d1 = n1 / baseLen;
            int d2 = n2 / baseLen;

            char* t1 = malloc((n1 + 1) * sizeof(char));
            char* t2 = malloc((n2 + 1) * sizeof(char));
            t1[0] = '\0';
            t2[0] = '\0';

            for(int j = 0; j < d1; j++) strcat(t1, base);
            for(int j = 0; j < d2; j++) strcat(t2, base);

            bool m1 = true;
            bool m2 = true;

            for(int k = 0; k < n1; k++){
                if(t1[k] != str1[k]){
                    m1 = false;
                    break;
                }
            }

            for(int k = 0; k < n2; k++){
                if(t2[k] != str2[k]){
                    m2 = false;
                    break;
                }
            }

            if(m1 && m2) break;
        }

        // Truncate string
        base[--baseLen] = '\0';

    }
    
    return base;
}

// --- 345. Reverse Vowels of a String ---
bool isVowel(char s){
    switch(tolower(s)){
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            return true;
        default:
            return false;
    }
}

char* reverseVowels(char* s){
    int n = strlen(s);

    int* indexes = (int*) calloc (n, sizeof(int));
    char* vowels = (char*) malloc ((n + 1) * sizeof(char));
    char* ans = (char*) malloc ((n + 1) * sizeof(char));

    // Collect indexes and vowels
    int j = 0;
    for(int i = 0; i < n; i++){
        char c = s[i];

        if(isVowel(c)){
            indexes[i] = 1;
            vowels[j++] = c;
        }
    }

    vowels[j] = '\0';

    // Reverse

    int i = 0;
    int k = strlen(vowels);

    while(i < n){
        if(indexes[i] == 0){
            ans[i] = s[i];
        } else {
            ans[i] = vowels[--k];
            printf("s[%d] = %c -> v[%d] = %c\n", i, s[i], k, vowels[k]);
        }

        i++;
    }

    ans[i] = '\0';

    return ans;

}

// --- 238. Product of Array Except Self ---
int* productExceptSelf(int* nums, int numsSize, int* returnSize){
    *returnSize = numsSize;

    int* answer = malloc(numsSize * sizeof(int));
        for(int i = 0; i < numsSize; i++){
            int sum = 1;
            for(int j = 0; j < numsSize; j++){
                if(i != j) sum *= nums[j];
            }
            answer[i] = sum;
        }

    return answer;
}

void test238(){
    int nums[] = {-1,1,0,-3,3};
    int numsSize = 5;

    print1DIntArray(nums, numsSize);

    int* rvSize = malloc(sizeof(int));
    int* rv = productExceptSelf(nums, numsSize, rvSize);

    print1DIntArray(rv, *rvSize);

    free(rv);
}

// --- 334. Increasing Triplet Subsequence ---
bool increasingTriplet(int* nums, int numsSize){
    int smallest = INT_MAX;
    int middle = INT_MAX;
    for(int i = 0; i < numsSize; i++){
        if(nums[i] <= smallest){
            smallest = nums[i];
        }
        else if(nums[i] <= middle){
            middle = nums[i];
        }
        else {
            return true;
        }
    }

    return false;
}

void test334(){
    int nums[] = {1,2,3,4,5};
    int numsSize = 5;
    bool rv = increasingTriplet(nums, numsSize);
    printf("rv = %d\n", rv);
}

// --- 5. Longest Palindromic Substring ---
void longestPalindromeHelper(char* s, int n, int* max, int* maxL, int* maxR, int l, int r){
    while(0 <= l && r < n && s[l] == s[r]){
        if(r - l + 1 > *max){
            *maxL = l;
            *maxR = r;
            *max = r - l + 1;
        }
        l--;
        r++;
    }
}

char* longestPalindrome(char* s){
    int n = strlen(s);
    char* res = malloc(n * sizeof(char) + 1);
    
    int l, r;
    int max = 0;
    int maxL = 0;
    int maxR = 0;

    for(int i = 0; i < n; i++){
        l = i;
        r = i;

        longestPalindromeHelper(s, n, &max, &maxL, &maxR, l, r);
    
        l = i;
        r = i + 1;
    
        longestPalindromeHelper(s, n, &max, &maxL, &maxR, l, r);
        
    }

    strncpy(res, s + maxL, maxR - maxL + 1);
    res[maxR - maxL + 1] = '\0';
    return res;
}

void test5(){
    char* str1 = longestPalindrome("babad");
    char* str2 = longestPalindrome("xabbayd");
    printf("Result: %s\n", str1);
    printf("Result: %s\n", str2);
}

// --- 443. String Compression ---

int compress(char* chars, int charsSize){
    int i = 0, res = -1;

    while(i < charsSize){
        int groupLength = 0;
        char letter = chars[i];
        while(i < charsSize && letter == chars[i]){
            groupLength++;
            i++;
        }
        // printf("[%c] %d\n", letter, groupLength);
        chars[++res] = letter;
        printf("[%d] = %c\n", res, letter);

        if(groupLength > 1){
            char groupLengthStr[10];
            sprintf(groupLengthStr, "%d", groupLength);
            for(int j = 0; j < strlen(groupLengthStr); j++){
                chars[++res] = groupLengthStr[j];
                printf("[%d] = %c\n", res, groupLengthStr[j]);
            }
        }
        
    }

    return ++res;
}

void test443(){
    char arr1[] = {'a', 'a', 'b', 'b', 'c', 'c', 'c'};
    char arr2[] = {'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'};
    char arr3[500]; for(int i = 0; i < 500; i++) arr3[i] = 'a';

    int n1 = compress(arr1, 7);


    printf("Result 1: %d\n", n1);
    printf("Result 1 str: ");
    for(int i = 0; i < n1; i++) printf("%c", arr1[i]);
    printf("\n");

    int n2 = compress(arr2, 13);

    printf("Result 2: %d\n", n2);
    printf("Result 2 str: ");
    for(int i = 0; i < n2; i++) printf("%c", arr2[i]);
    printf("\n");

    int n3 = compress(arr3, 500);

    printf("Result 3: %d\n", n3);
    printf("Result 3 str: ");
    for(int i = 0; i < n3; i++) printf("%c", arr3[i]);
    printf("\n");
}

// --- 283. Move Zeroes ---

void moveZeroes(int* nums, int numsSize){
    int numZeroes = 0;

    // O(n)
    for(int i = 0; i < numsSize; i++) if(nums[i] == 0) numZeroes++;
    
    // O(n^2)
    for(int i = 0; i < numsSize; i++){
        for(int j = i; j < numsSize; j++){
            if(nums[j] != 0){
                int t = nums[j];
                nums[j] = 0;
                nums[i] = t;
                break;
            }
        }
    }

    // O(n)
    for(int i = numsSize - numZeroes; i < numsSize; i++) nums[i] = 0;
}

void test283(){
    int nums1[] = {0,1,0,3,12};
    int nums2[] = {0};
    int nums1Size = 5;
    int nums2Size = 1;

    moveZeroes(nums1, nums1Size);
    moveZeroes(nums2, nums2Size);

    printf("Result 1: ");
    print1DIntArray(nums1, nums1Size);
    printf("Result 2: ");
    print1DIntArray(nums2, nums2Size);

}

// --- 392. Is Subsequence ---
bool isSubsequence(char* s, char* t) {
    int s_len = strlen(s);
    int t_len = strlen(t);

    int next = -1;
    int k = 0;
    
    if(k == s_len) return true;

    for(int i = 0; i < t_len; i++){
        // Find first char
        if(t[i] == s[0]){
            // Begin scanning
            int k = 1;

            for(int j = i + 1; j < t_len; j++){
                if(next == -1 && t[j] == t[i]) next = j;
                if(k < s_len && t[j] == s[k]) k++;
            }

            // Check if target found
            if(k == s_len) return true;
            
            // Reset
            k = 0;
            i = (next == -1) ? i : next - 1;
            next = -1;
        }
    }
    return false;
}

// Optimal solution
bool isSubsequenceV2(char* s, char* t){
    int i = 0;
    int j = 0;
    
    while(s[i] && t[j]){
        if(s[i] == t[j]) i++;
        j++;
    }

    return s[i] == '\0';

}

void test392(){
    char* s1 = "abc";
    char* t1 = "ahbdgc";

    char* s2 = "axc";
    char* t2 = "ahbgdc";

    char* s3 = "";
    char* t3 = ";fsdjkla";

    printf("Result 1: %d\n", isSubsequenceV2(s1, t1));
    printf("Result 2: %d\n", isSubsequenceV2(s2, t2));
    printf("Result 3: %d\n", isSubsequenceV2(s3, t3));
}

int main(int argc, char* argv[]){
    test392();
}