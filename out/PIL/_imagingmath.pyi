from typing import Any

abs_F: int
abs_I: int
add_F: int
add_I: int
and_I: int
diff_F: int
diff_I: int
div_F: int
div_I: int
eq_F: int
eq_I: int
ge_F: int
ge_I: int
gt_F: int
gt_I: int
invert_I: int
le_F: int
le_I: int
lshift_I: int
lt_F: int
lt_I: int
max_F: int
max_I: int
min_F: int
min_I: int
mod_F: int
mod_I: int
mul_F: int
mul_I: int
ne_F: int
ne_I: int
neg_F: int
neg_I: int
or_I: int
pow_F: int
pow_I: int
rshift_I: int
sub_F: int
sub_I: int
xor_I: int

def binop(*args, **kwargs) -> Any: ...
def unop(*args, **kwargs) -> Any: ...
