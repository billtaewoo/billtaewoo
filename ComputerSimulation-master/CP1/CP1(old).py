# from polynomial import polynomial
from new_poly import Poly

def main():
    eq = Poly([2,0,4,-1,0,6])
    eq.O()
    eq.Add([-1,-3,0,4.5,0,0])
    eq.Der()
    eq.Int([0, 8, -3, 0, 30], 2)
    
    # MyEq = polynomial([2,0,4,-1,0,6])
    # print("Order of Pa(x) is "+ str(MyEq.order_list())) # print order
    # MyEq.add_list([-1,-3,0,4.5,0,0]) # print adding polynomial
    # poly_1_diff = MyEq.diff_list() # print differentiated coefficient
    # # print(poly_1_diff = MyEq.diff_list())
    # poly_1_diff.int_list(2)
    # print(MyEq.int_list(2).pirnt_poly()) # print integrate coefficient

main()
