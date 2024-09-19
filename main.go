package main

import (
	"encoding/csv"
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)

func readCSV(filePath string) ([][]string, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, fmt.Errorf("failed to open CSV file: %w", err)
	}
	defer file.Close()

	reader := csv.NewReader(file)
	records, err := reader.ReadAll()
	if err != nil {
		return nil, fmt.Errorf("failed to read CSV file: %w", err)
	}

	return records, nil
}

func findColumnIndex(header []string, columnName string) int {
	for i, colName := range header {
		if colName == columnName {
			return i
		}
	}
	return -1
}

func extractUniqueValues(records [][]string, columnIndex int) []string {
	uniqueValues := make(map[string]bool)
	var result []string

	for _, record := range records[1:] {
		if len(record) > columnIndex {
			value := strings.TrimSpace(record[columnIndex])
			if value != "" && !uniqueValues[value] {
				uniqueValues[value] = true
				result = append(result, value)
			}
		}
	}

	return result
}

func formatOutput(urls []string, project string) string {
	if len(urls) == 0 {
		return "No valid URLs found."
	}
	return fmt.Sprintf("project = %s AND issuekey in (%s)", project, strings.Join(urls, ", "))
}

func main() {

	project := flag.String("project", "OCPBUGS", "The project name (OCPBUGS, RHEL, RHELPLAN)")
	flag.Parse()

	args := flag.Args()
	if len(args) < 1 {
		log.Fatalf("Usage: %s -project=RHEL <path to csv file>", os.Args[0])
	}

	filePath := args[0]

	records, err := readCSV(filePath)
	if err != nil {
		log.Fatalf("Error: %s", err)
	}

	if len(records) == 0 {
		log.Fatalf("CSV file is empty")
	}

	urlIndex := findColumnIndex(records[0], "Resource URL")
	if urlIndex == -1 {
		log.Fatalf("No 'Resource URL' column found in this CSV file.")
	}

	urls := extractUniqueValues(records, urlIndex)

	fmt.Println(formatOutput(urls, *project))
}
