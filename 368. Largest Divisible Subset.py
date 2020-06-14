class Node:
    def __init__(self, val, depth, subset):
        self.val = val
        self.depth = depth
        self.children = []
        self.subset = subset


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        def traverse(node, val):
            add_child = True
            for child in node.children:
                if not val % child.val:
                    # current value is divisible by value of child node
                    traverse(child, val)
                    # if we found a child node, then we do not want to add a node
                    # since it will have a lower depth
                    add_child = False
					
            if add_child:
                # add as child to current node since current value is not divisible by any child
                new_node = Node(val, node.depth + 1, node.subset + [val])
                node.children.append(new_node)
				
                # check if new node has biggest subset
                if new_node.depth > max_depth[0]:
                    max_depth[0] = new_node.depth
                    max_depth_node[0] = new_node
					
		# handle trivial cases of empty input and single value
        if len(nums) < 2:
            return nums

        # we require a sorted list for processing
        nums = sorted(nums)

        # create root node with value 1 since all other values are divisible by 1
        # check if 1 is in nums, if not, add it but with depth 0 instead of 1 (and empty subset)
        if nums[0] != 1:
            root = Node(val=1, depth=0, subset=[])
        else:
            root = Node(val=1, depth=1, subset=[1])

        # track node with maximum depth
        max_depth_node = [root]
        # track maximum depth (= length of subset) to not recalculate from subset length
        max_depth = [0]

        for num in nums[root.depth:]:
            traverse(root, num)

		# return largest subset
        return max_depth_node[0].subset