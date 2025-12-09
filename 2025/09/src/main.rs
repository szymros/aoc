fn part1(input: &str) -> u64 {
    let input = input
        .lines()
        .map(|line| {
            line.split(",")
                .map(|val| val.parse::<i64>().unwrap())
                .collect::<Vec<i64>>()
        })
        .collect::<Vec<Vec<i64>>>();
    let mut largest = 0;
    for xy in input.iter() {
        for inner in input.iter() {
            let area = (xy[0].abs_diff(inner[0]) + 1) * (xy[1].abs_diff(inner[1]) + 1);
            if area > largest {
                largest = area;
            }
        }
    }
    return largest;
}

fn part2(input: &str) -> u64 {
    let input = input
        .lines()
        .map(|line| {
            line.split(",")
                .map(|val| val.parse::<i64>().unwrap())
                .collect::<Vec<i64>>()
        })
        .collect::<Vec<Vec<i64>>>();
    let mut other = input[1..].to_vec();
    other.push(input[0].clone());
    let mut row_ranges: Vec<((i64, i64), (i64, i64))> = Vec::new();
    let mut column_ranges: Vec<((i64, i64), (i64, i64))> = Vec::new();
    for (lhs, rhs) in input.iter().zip(other.iter()) {
        if lhs[0] == rhs[0] {
            let r = if lhs[1] < rhs[1] {
                ((lhs[0], lhs[1]), (rhs[0], rhs[1]))
            } else {
                ((rhs[0], rhs[1]), (lhs[0], lhs[1]))
            };
            column_ranges.push(r);
        } else {
            let r = if lhs[0] < rhs[0] {
                ((lhs[0], lhs[1]), (rhs[0], rhs[1]))
            } else {
                ((rhs[0], rhs[1]), (lhs[0], lhs[1]))
            };
            row_ranges.push(r);
        }
    }
    let mut largest = 0;
    for xy in input.iter() {
        for inner in input.iter() {
            let corners = [(xy[0], inner[1]), (inner[0], xy[1])];
            let mut fits = [false, false];
            for (i, c) in corners.iter().enumerate() {
                let mut low_bound_x = false;
                let mut high_bound_x = false;
                let mut low_bound_y = false;
                let mut high_bound_y = false;
                for r in row_ranges.iter() {
                    let (start, end) = r;
                    if c.0 >= start.0 && c.0 <= end.0 {
                        if start.1 == c.1 {
                            low_bound_y = true;
                            high_bound_y = true;
                        }
                        if start.1 < c.1 {
                            low_bound_x = true;
                        } else {
                            high_bound_x = true;
                        }
                    }
                }
                for r in column_ranges.iter() {
                    let (start, end) = r;
                    if c.1 >= start.1 && c.1 <= end.1 {
                        if start.0 == c.0 {
                            low_bound_y = true;
                            high_bound_y = true;
                        }
                        if start.0 < c.0 {
                            low_bound_y = true;
                        } else {
                            high_bound_y = true;
                        }
                    }
                }
                if high_bound_x && low_bound_x && high_bound_y && low_bound_y {
                    fits[i] = true;
                }
            }
            if fits.iter().all(|b| *b) {
                let area = (xy[0].abs_diff(inner[0]) + 1) * (xy[1].abs_diff(inner[1]) + 1);
                if area > largest {
                    largest = area;
                }
            }
        }
    }
    return largest;
}
fn main() {
    let input = std::fs::read_to_string("test_input.txt").unwrap();
    println!("part 1 {}", part1(&input));
    println!("part 2 {}", part2(&input));
}
