#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

// --- 1071. Greatest Common Divisor of Strings
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





int main(int argc, char* argv[]){
    printf("%s\n", reverseVowels("IceCreAm"));
}