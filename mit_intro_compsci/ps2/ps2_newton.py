# 6.00 Problem Set 2
#
# Successive Approximation
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    # ans = 0.0
    # index = 0
    #
    # for i in poly:
    #     term = i * (x ** index)
    #     index += 1
    #     ans = ans + term
    #
    # return ans

    total = 0.0
    for i  in xrange(len(poly)):
        total += poly[i] * (x ** i)
    return total


print evaluate_poly((0.0, 0.0, 5.0, 9.3, 7.0), -13)


#
# print "evaluate_poly:", evaluate_poly((0.0, 0.0, 5.0, 9.3, 7.0), -13)

#
# #
# #
# def compute_deriv(poly):
#     """
#     Computes and returns the derivative of a polynomial function. If the
#     derivative is 0, returns (0.0,).
#
#     Example:
#     >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
#     >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
#     (0.0, 35.0, 9.0, 4.0)
#
#     poly: tuple of numbers, length > 0
#     returns: tuple of numbers
#     """
#     # f(x) = ax^b f'(x)= abx^b-1
#     ans = ()
#     index = 0
#
#     for i in poly:
#         deriv = round(i * index, 2)
#
#         if index == 0:
#             pass
#         elif deriv == 0:
#             ans = ans + (0.0, )
#         else:
#             ans = ans + (deriv, )
#
#         index += 1
#
#     print ans
# #
# #
# ##print compute_deriv((-13.39, 0.0, 17.5, 3.0, 1.0))
# #
# #
# # #print compute_deriv((2.3, 124.5, 12, 35, 1, 4.2, 64.1, 8.9))
# #
# # function = ()
# #
# # number = input("Please enter the number of terms in the function (including those equal to zero): ")
# #
# #
# # for i in range(0, number):
# #     if i == 0:
# #         term = float(raw_input("Please enter the coefficient of the first term (lowest power): "))
# #     else:
# #         term = float(raw_input("Please enter the coefficient of the next term: "))
# #
# #     function = function + (term, )
# #
# # print "Function: ", function
# #
# # print "Derivative: ", compute_deriv(function)
#
#
# def compute_root(poly, x_0, epsilon):
#     """
#     Uses Newton's method to find and return a root of a polynomial function.
#     Returns a tuple containing the root and the number of iterations required
#     to get to the root.
#
#     Example:
#     >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
#     >>> x_0 = 0.1
#     >>> epsilon = .0001
#     >>> print compute_root(poly, x_0, epsilon)
#     (0.80679075379635201, 8.0)
#
#     poly: tuple of numbers, length > 1.
#          Represents a polynomial function containing at least one real root.
#          The derivative of this polynomial function at x_0 is not 0.
#     x_0: float
#     epsilon: float > 0
#     returns: tuple (float, int)
#     """
#     # TO DO ...
#
#     function = ()
#     deriv = ()
#     attempt = 1
#     assert x_0 != 0
#
#     # Evaluate function at x_0
#     function = evaluate_poly(poly, x_0)
#
#     # Check whether function is close enough to zero
#
#     while abs(function) > epsilon:
#             attempt += 1
#             deriv = compute_deriv(poly)
#             x_0 = x_0 - (function /evaluate_poly(deriv, x_0))
#             function = evaluate_poly(poly, x_0)
#
#     return (x_0, attempt)
#
#
# print compute_root((-13.39, 0.0, 17.5, 3.0, 1.0), 0.1, .0001)
#
# print "program finished."
# #
