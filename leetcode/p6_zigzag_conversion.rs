impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1{
            return s;
        }

        // return string
        let mut zigzag_string = String::from("");

        // string to Vec<char>
        let myString: Vec<char> = s.chars().collect();

        let num_rows: usize = num_rows as usize;
        // calculate chunk size and length!
        let chunk_size = 2 * (num_rows - 1);
        let mut chunk_length = myString.len() / chunk_size;
        let rest = myString.len() % chunk_size;
        let stringLength = myString.len();

        let mut targetIndexContainer:Vec<usize> = Vec::new();
        if rest > 0{
            chunk_length += 1;
        }

        // ROW 개수
        for row in 0..num_rows{
            // 메모리 청크 개수
            for index  in 0..chunk_length{
                if row == 0{
                    targetIndexContainer.push(chunk_size * index);
                }
                else if row == num_rows-1{
                    targetIndexContainer.push(chunk_size * index + row);
                }
                else{
                    targetIndexContainer.push(chunk_size * index + row);
                    targetIndexContainer.push(chunk_size * (index+1) - row);
                }
            }

            for target in targetIndexContainer.iter(){
                if *target < stringLength{
                    zigzag_string.push_str(&myString[*target].to_string());
                }
            }
            targetIndexContainer.clear();
        }

        return zigzag_string;
    }
}