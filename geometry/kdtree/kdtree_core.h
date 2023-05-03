#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <float.h>

// Forward decl
void get_bounding_box(float *points, uint32_t *pidx, int8_t dim, float *bbox);
void create_kdtree(float *points, uint8_t dim, uint32_t length);