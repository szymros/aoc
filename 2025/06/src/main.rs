use std::collections::HashMap;

fn part1(input: &str) -> i64 {
    let mut lines = input
        .lines()
        .map(|line| line.split_whitespace().collect::<Vec<&str>>())
        .collect::<Vec<Vec<&str>>>();
    let lines_len = lines.len();
    let mut number_columns: HashMap<usize, Vec<i64>> = HashMap::new();
    lines[..lines_len - 1].iter_mut().for_each(|line| {
        line.iter().enumerate().for_each(|(num_idx, value)| {
            let parsed = value.parse::<i64>().unwrap();
            number_columns
                .entry(num_idx)
                .and_modify(|value| value.push(parsed))
                .or_insert(vec![parsed]);
        })
    });
    let operators = lines.last().unwrap();
    let mut output = 0;
    number_columns.iter().for_each(|(column, values)| {
        let operator = match operators.get(*column) {
            Some(&"*") => |lhs: i64, rhs: i64| -> i64 { lhs * rhs },
            _ => |lhs: i64, rhs: i64| -> i64 { lhs + rhs },
        };
        let v = values.iter().copied().reduce(operator).unwrap();
        output += v;
    });
    return output;
}

fn part2(input: &str) -> i64 {
    let mut columns: HashMap<usize, String> = HashMap::new();
    input.lines().for_each(|line| {
        if line.contains(['*', '+']) {
            return;
        }
        line.char_indices().for_each(|(idx, c)| {
            columns
                .entry(idx)
                .and_modify(|s| s.push(c))
                .or_insert(c.to_string());
        })
    });
    columns.retain(|_, val| !val.trim().is_empty());
    let mut keys = columns.keys().copied().collect::<Vec<usize>>();
    keys.sort();
    let line_with_operators = input.lines().last().unwrap().to_string();
    let mut output = 0;
    let mut temp: Vec<i64> = Vec::new();
    keys.iter().rev().for_each(|key| {
        temp.push(columns.get(key).unwrap().trim().parse::<i64>().unwrap());
        let operator = line_with_operators.get(*key..*key + 1).unwrap();
        if operator.contains(['*', '+']) {
            let operator_func = match Some(operator) {
                Some("*") => |lhs: i64, rhs: i64| -> i64 { lhs * rhs },
                _ => |lhs: i64, rhs: i64| -> i64 { lhs + rhs },
            };
            output += temp.iter().cloned().reduce(operator_func).unwrap_or(0);
            temp = vec![];
        }
    });
    return output;
}

fn main() {
    let input = std::fs::read_to_string("input.txt").unwrap();
    println!("part 1 {}", part1(&input));
    println!("part 2 {}", part2(&input));
}
