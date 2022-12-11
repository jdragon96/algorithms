fn selection_sorting(mut arr: Vec<i32>) -> Vec<i32>{
  let arr_length = arr.len();

  for i in 0..arr_length{
    let mut min_index = i;
    // 최소값 index 찾기
    for j in (i+1)..arr_length{
      if (arr[min_index] > arr[j]){
        min_index = j
      }
    }

    // 교체
    let temp = arr[min_index];
    arr[min_index] = arr[i];
    arr[i] = temp;
  }
  
  arr
}