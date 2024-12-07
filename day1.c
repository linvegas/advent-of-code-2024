#include <stdio.h>

void list_sort(int *list, int len)
{
    for (int i = 0; i < len; i++) {
        for (int j = 0; j < len - 1; j++) {
            if (list[j] > list[j+1]) {
                int temp = list[j];
                list[j] = list[j+1];
                list[j+1] = temp;
            }
        }
    }
}

void list_print(int *list, int len)
{
    for (int i = 0; i < len; i++) {
        printf("%d ", list[i]);
    }
    printf("\n");
}

int main()
{
    int left_list[6];
    int right_list[6];

    FILE *file = fopen("day1.txt", "r");

    char c;
    int i;
    while ((c = fgetc(file)) != EOF) {
        if (c == ' ' || c == '\n') continue;

        if (i % 2 == 0) left_list[i/2] = c - '0';
        else right_list[i/2] = c - '0';

        i += 1;
    }

    fclose(file);

    list_sort(left_list, 6);
    list_sort(right_list, 6);

    int total_distance = 0;

    for (int i = 0; i < 6; i++) {
        if (left_list[i] > right_list[i])
            total_distance += left_list[i] - right_list[i];
        else
            total_distance += right_list[i] - left_list[i];
    }

    printf("total distance is %d\n", total_distance);

    return 0;
}
