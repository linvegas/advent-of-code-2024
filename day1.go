package main

import (
    "fmt"
    "sort"
)

func main() {
    var leftList = []int{3, 4, 2, 1, 3, 3}
    var rightList = []int{4, 3, 5, 3, 9, 3}

    sort.Ints(leftList)
    sort.Ints(rightList)

    var totalDistance = 0

    for i := range(leftList) {
        if leftList[i] > rightList[i] {
            totalDistance += leftList[i] - rightList[i]
        } else {
            totalDistance += rightList[i] - leftList[i]
        }
    }

    fmt.Println(totalDistance)
}
