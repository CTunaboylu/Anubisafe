#ifndef _BODY_OF_ANUBIS
#define _BODY_OF_ANUBIS
#include "anubis.hpp"

extern "C" {
// libecc library inclusions for c linkage 
#include "libec.h"

}
Curve::Curve(bool __def, ){
this.__default = __def;
}

extern "C" {

int fp_square_root(fp_t sqrt1, fp_t sqrt2, fp_src_t n);
void get_random_point_on_curve(ec_params *curve_params, prj_pt *out_point);

}  
//4a³+27b² ≠ 0
inline int Curve::avoid_singularity(int &a, int &b) const {
	int t_a = 2*a;
	int t_b = 3*b;
	t_a = (t_a)*a;
	t_b = (t_b)*(t_b)*(-3);
	return (t_a == t_b); 
}
inline void get_random_point_on_curve(ec_params *curve_params, prj_pt *out_point)
{
	nn nn_tmp;
	/* Inside internal representation, curve_params->ec_curve
	 * contains the curve coefficients a and b.
	 * curve_params->ec_fp is the Fp context of the curve.
	 */
	fp x, y, fp_tmp1, fp_tmp2;
	fp_ctx_src_t ctx;
	/* Initialize our x value with the curve Fp context */
	ctx = &(curve_params->ec_fp);
	fp_init(&x, ctx);
	fp_init(&y, ctx);
	fp_init(&fp_tmp1, ctx);
	fp_init(&fp_tmp2, ctx);

	nn_init(&nn_tmp, 0);
	nn_set_word_value(&nn_tmp, WORD(3));
	while (1) {
		/* Get a random Fp */
		fp_get_random(&x, ctx);
		fp_copy(&fp_tmp1, &x);
		fp_copy(&fp_tmp2, &x);
		/* Compute x^3 + ax + b */
		fp_pow(&fp_tmp1, &fp_tmp1, &nn_tmp);
		fp_mul(&fp_tmp2, &fp_tmp2, &(curve_params->ec_curve.a));
		fp_add(&fp_tmp1, &fp_tmp1, &fp_tmp2);
		fp_add(&fp_tmp1, &fp_tmp1, &(curve_params->ec_curve.b));
		/*
		 * Get any of the two square roots, corresponding to (x, y)
		 * and (x, -y) both on the curve. If no square root exist,
		 * go to next random Fp.
		 */
		if (fp_square_root(&y, &fp_tmp2, &fp_tmp1) == 0) {
			/* Check that we indeed satisfy the curve equation */
			if (!is_on_curve(&x, &y, &(curve_params->ec_curve))) {
				/* This should not happen ... */
				ext_printf("Error: Tonelli-Shanks found a bad "
					   "solution to curve equation ...\n");
				continue;
			}
			break;
		}
	}
	/* Now initialize our point with the coordinates (x, y, 1) */
	fp_one(&fp_tmp1);
	prj_pt_init_from_coords(out_point, &(curve_params->ec_curve), &x, &y,
				&fp_tmp1);

	fp_uninit(&x);
	fp_uninit(&y);
	fp_uninit(&fp_tmp1);
	fp_uninit(&fp_tmp2);
	nn_uninit(&nn_tmp);
}
#endif
