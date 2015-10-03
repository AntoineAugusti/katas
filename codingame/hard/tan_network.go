package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func DegreeToRadian(d float64) float64 {
	return d * math.Pi / 180
}

type Station struct {
	name      string
	latitude  float64
	longitude float64
}

type Destination struct {
	code string
	cost float64
}

func ToFloat(s string) (res float64) {
	res, _ = strconv.ParseFloat(s, 64)
	return
}

func Distance(a, b Station) float64 {
	x := (b.longitude - a.longitude) * math.Cos((a.latitude+b.latitude)/2)
	y := b.latitude - a.latitude
	return math.Sqrt(x*x+y*y) * 6371
}

func Travel(cost float64, route []string, end string) {
	for _, destination := range routes[route[len(route)-1]] {
		if cost += destination.cost; cost < minCost {
			mcValue, mcOK := stationsMC[destination.code]
			if (mcOK && cost < mcValue) || !mcOK {
				stationsMC[destination.code] = cost
				if destination.code == end {
					minCost = cost
					finalRoute = append(route, destination.code)
				} else {
					Travel(cost, append(route, destination.code), end)
				}
			}
		}
	}
}

var minCost float64 = math.MaxFloat64

// Associate station codes and station objects
var stations map[string]Station = make(map[string]Station)

// Associate station codes and immediately reachable destinations
var routes map[string][]Destination = make(map[string][]Destination)

// A list of station codes
var finalRoute []string

// Associate station codes and costs
var stationsMC map[string]float64 = make(map[string]float64)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	// Read start and end points
	var start string
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &start)

	var end string
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &end)

	// Read stations
	var nbStations int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &nbStations)
	for i := 0; i < nbStations; i++ {
		scanner.Scan()
		station := scanner.Text()
		parts := strings.Split(station, ",")
		stations[parts[0]] = Station{
			parts[1][1 : len(parts[1])-1],
			DegreeToRadian(ToFloat(parts[3])),
			DegreeToRadian(ToFloat(parts[4])),
		}
	}

	// Case start point == end point
	if start == end {
		fmt.Println(stations[start].name)
		return
	}

	// Read routes
	var nbRoutes int
	scanner.Scan()
	fmt.Sscan(scanner.Text(), &nbRoutes)
	for i := 0; i < nbRoutes; i++ {
		scanner.Scan()
		route := scanner.Text()
		parts := strings.Split(route, " ")
		a, b := parts[0], parts[1]

		cost := Distance(stations[a], stations[b])
		routes[a] = append(routes[a], Destination{b, cost})
	}

	// Find the solution
	Travel(0, append(make([]string, 0), start), end)

	// Print the solution
	if finalRoute == nil {
		fmt.Println("IMPOSSIBLE\n")
	} else {
		for _, code := range finalRoute {
			fmt.Println(stations[code].name)
		}
	}
}
