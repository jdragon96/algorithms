#include "kdtree_core.h"

#define PA(i,d) (pa[no_dims * pidx[i] + d])

void 
create_kdtree(float *points, uint8_t dim, uint32_t length){
  // 0. 포인트 index용 배열 생성
  uint32_t *point_index = (uint32_t)malloc(sizeof(uint32_t) * length);
  for(int i=0; i<length; ++i){
    point_index[i] = i;
  }

  // 1. BBox 메모리 할당
  float *bbox = (float*)malloc(2 * sizeof(float) * dim);
  get_bounding_box(points, point_index, dim, bbox);
  
  // 2. KdTree 생성 시작
}

// BBox = [minx, miny, minz, maxx, maxy, maxz]
void 
get_bounding_box(float *points, uint32_t *pidx, int8_t dim, float *bbox){

}