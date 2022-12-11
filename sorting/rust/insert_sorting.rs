fn insert_sorting(mut arr: Vec<i32>) -> Vec<i32>{
  let arr_length = arr.len();

  for i: i32 in 1..arr_length{
    let mut cur_index: i32 = i;

    // 정렬하기
    while (cur_index > 0){
      if (arr[cur_index-1] > arr[cur_index]){
        let temp = arr[cur_index];
        arr[cur_index] = arr[cur_index-1];
        arr[cur_index-1] = temp;
      }
      cur_index -= 1;
    }
  }

  arr
}
