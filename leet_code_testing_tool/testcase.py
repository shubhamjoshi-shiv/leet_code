def run_test_case():
            s = Solution()
    
            # Example 1
            result = s.longestConsecutive(nums = [100,4,200,1,3,2])
            output_param = 4
            if result != output_param:
                print('expected result -',output_param)
                print('got result -',result)
            else:
                print('tc passed')
            
            # Example 2
            result = s.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])
            output_param = 9
            if result != output_param:
                print('expected result -',output_param)
                print('got result -',result)
            else:
                print('tc passed')
            
            # Example 3
            result = s.longestConsecutive(nums = [0,100,7,2,5,8,4,6,0,1])
            output_param = 5
            if result != output_param:
                print('expected result -',output_param)
                print('got result -',result)
            else:
                print('tc passed')
            
            # Example 4
            result = s.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1,-1,-2])
            output_param = 11
            if result != output_param:
                print('expected result -',output_param)
                print('got result -',result)
            else:
                print('tc passed')
            
run_test_case()