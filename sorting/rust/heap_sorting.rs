fn heapify(arr:&mut Vec<i32>, start_index: usize, length: usize){
  let mut s_idx = start_index;
  let left_idx = start_index * 2 + 1;
  let right_idx = start_index * 2 + 2;

  if((left_idx < length) && (arr[s_idx] < arr[left_idx])){
    s_idx = left_idx;
  }

  if((right_idx < length) && (arr[s_idx] < arr[right_idx])){
    s_idx = right_idx
  }

  if(s_idx != start_index){
    arr.swap(start_index, s_idx);
    heapify(arr, s_idx, length);
  }
}
fn heap_sorting(arr: &mut Vec<i32>){
  let mut l = arr.len() as i32;
  let mut i: i32 = (l/2)-1;
  loop{
    if i < 0{
      break;
    }
    heapify(arr, i as usize, l as usize);
    i -= 1;
  }

  let mut extract_index: i32 = arr.len() as i32 - 1;
  loop{
    if extract_index < 0{
      break
    }
    arr.swap(0, extract_index as usize);
    heapify(arr, 0 as usize, extract_index as usize);
    extract_index -= 1;
  }
}
