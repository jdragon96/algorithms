fn bubble_sorting(mut arr: Vec<i32>) -> Vec<i32> {
  let arr_length: usize = arr.len();
  for i in 0..arr_length{
      
      for j in 1..arr_length-i{
          // 1. j-1이 j보다 큰 경우
          if(arr[j-1] > arr[j]){
              // 스왑하기
              let temp = arr[j];
              arr[j] = arr[j-1];
              arr[j-1] = temp
          }
      }
  }
  return arr
}

// fn main() {
//   let v: Vec<i32> = vec![1,5,4,6,8,0,9];
//   let r = bubble_sorting(v);
//   println!("{:?}", r);
// }