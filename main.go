package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
)

func main() {
	file, err := os.Open("data.csv")
	if err != nil {
		log.Fatalf("Failed to open csv file: %s", err)
	}
	defer file.Close()

	reader := csv.NewReader(file)

	records, err := reader.ReadAll()
	if err != nil {
		log.Fatalf("failed to read csv file: %s", err)
	}

	for _, record := range records {
		fmt.Println(record)
	}

}
