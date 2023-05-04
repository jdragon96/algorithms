fn zigzag(rows: i32) -> impl Iterator<Item = i32> {
    (0..rows - 1).chain((1..rows).rev()).cycle()
}

fn main(){
    let s = String::from("ABCDE");
    let num_rows = 3;
    let mut rails: Vec<Vec<char>> = vec![vec![]; num_rows as usize];
    // let mut rails: Vec<char> = vec![]; num_rows as usize;

    for (ch, rail) in s.chars().zip(zigzag(num_rows)){
        rails[rail as usize].push(ch);
    }

    let mut result = String::from("");
    for i in rails{
        for j in i{
            result.push_str(&j.to_string());
        }
    }
    println!("{}", result);
}