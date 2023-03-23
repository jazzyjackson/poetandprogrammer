//write a program that takes 3 words as user input and fills them into a predefined madlib

package main

//importing fmt package
import "fmt"
//importing bufio package
import "bufio"
//importing os package
import "os"
//importing strings package
import "strings"

//main function
func main() {
	//declaring variables
	var madlib string
	var word1 string
	var word2 string
	var word3 string
	//declaring a scanner
	scanner := bufio.NewScanner(os.Stdin)
	//printing the madlib
	fmt.Println("A vacation is when you take a trip to some", word1, "place with your", word2, "family. Usually you go to some place that is near a/an", word3, "or up on a mountain.")
	//asking for user input
	fmt.Println("Enter a word:")
	//scanning the input
	scanner.Scan()
	//storing the input in word1
	word1 = scanner.Text()
	//asking for user input
	fmt.Println("Enter a word:")
	//scanning the input
	scanner.Scan()
	//storing the input in word2
	word2 = scanner.Text()
	//asking for user input
	fmt.Println("Enter a word:")
	//scanning the input
	scanner.Scan()
	//storing the input in word3
	word3 = scanner.Text()
	//replacing the words in the madlib
	madlib = strings.Replace("A vacation is when you take a trip to some", word1, "place with your", word2, "family. Usually you go to some place that is near a/an", word3, "or up on a mountain.", "word1", -1)
	madlib = strings.Replace(madlib, "word2", word2, -1)
	madlib = strings.Replace(madlib, "word3", word3, -1)
	//printing the madlib
	fmt.Println(madlib)
}

