package main

import "fmt"

// Define an interface
type Shape interface {
	Area() float64
	Perimeter() float64
}

// Struct that implements Shape
type Rectangle struct {
	Width, Height float64
}

func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

func (r Rectangle) Perimeter() float64 {
	return 2 * (r.Width + r.Height)
}

func printShapeInfo(s Shape) {
	fmt.Println("Area:", s.Area())
	fmt.Println("Perimeter:", s.Perimeter())
}

func main() {
	r := Rectangle{Width: 10, Height: 5}
	printShapeInfo(r)
}
