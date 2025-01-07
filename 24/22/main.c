#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <sys/time.h>
#include <omp.h>

#define WALLTIME(t) ((double)(t).tv_sec + 1e-6 * (double)(t).tv_usec)

#define DATA_LENGTH 1515
#define SEQUENCE_LENGTH 4
#define MAX_ITERATIONS 2000

uint64_t mix(uint64_t secret_num, uint64_t value) {
    return secret_num ^ value;
}

uint64_t prune(uint64_t secret_num) {
    return secret_num % 16777216;
}

uint64_t next_secret_num(uint64_t secret_num) {
    uint64_t res = prune(mix(secret_num, secret_num << 6));
    res = prune(mix(res, res >> 5));
    res = prune(mix(res, res << 11));
    return res;
}

void load_data(const char *filename, uint64_t *data) {
    FILE *file = fopen(filename, "r");

    int index = 0;
    while (fscanf(file, "%lu", &data[index]) == 1) {
        index++;
    }
    fclose(file);
}

uint64_t part1(uint64_t *data) {
    long long sum = 0;
    for (int i = 0; i < DATA_LENGTH; i++) {
        uint64_t num = data[i];
        for (int j = 0; j < MAX_ITERATIONS; j++) {
            num = next_secret_num(num);
        }
        sum += num;
    }
    return sum;
}

uint64_t part2(uint64_t *data) {

    int **prices = (int **)malloc(DATA_LENGTH * sizeof(int *));
    int **changes = (int **)malloc(DATA_LENGTH * sizeof(int *));

    for (int i = 0; i < DATA_LENGTH; i++) {
        prices[i] = (int *)calloc(MAX_ITERATIONS + 1, sizeof(int));
        changes[i] = (int *)calloc(MAX_ITERATIONS + 1, sizeof(int));

        uint64_t num = data[i];
        prices[i][0] = num % 10;
        changes[i][0] = 0;

        for (int j = 1; j <= MAX_ITERATIONS; j++) {
            num = next_secret_num(num);
            prices[i][j] = num % 10;
            changes[i][j] = prices[i][j] - prices[i][j - 1];
        }
    }
    int best = 0;

    #pragma omp parallel for collapse(4)
    for (int seq0 = -9; seq0 <= 9; seq0++) {
        for (int seq1 = -9; seq1 <= 9; seq1++) {
            for (int seq2 = -9; seq2 <= 9; seq2++) {
                for (int seq3 = -9; seq3 <= 9; seq3++) {
                    int local_sequence[SEQUENCE_LENGTH] = {seq0, seq1, seq2, seq3};

                    int score = 0;
                    for (int i = 0; i < DATA_LENGTH; i++) {

                        for (int j = SEQUENCE_LENGTH; j <= MAX_ITERATIONS; j++) {
                            int match = 1;
                            for (int k = 0; k < SEQUENCE_LENGTH; k++) {
                                if (changes[i][j - 3 + k] != local_sequence[k]) {
                                    match = 0;
                                    break;
                                }
                            }
                            if (match) {
                                score += prices[i][j];
                                break;
                            }
                        }
                    }
                    #pragma omp critical
                    if (score > best) {
                        best = score;
                    }
                }
            }
        }
    }
    for (int i = 0; i < DATA_LENGTH; i++) {
        free(prices[i]);
        free(changes[i]);
    }
    free(prices);
    free(changes);

    return best;
}

int main() {
    struct timeval t_start, t_end;
    gettimeofday ( &t_start, NULL );

    const char *filename = "input.txt";
    uint64_t data[DATA_LENGTH];
    load_data(filename, data);

    printf("---MAIN---\n");
    printf("part 1: %lu\n", part1(data));
    printf("part 2: %lu\n", part2(data));

    gettimeofday ( &t_end, NULL );
    printf ( "Total elapsed time: %lf seconds\n",
        WALLTIME(t_end) - WALLTIME(t_start)
    );

    return 0;
}
