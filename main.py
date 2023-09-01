def printCorner(root):

    if root == None:
        return

    q = []
    q.append(root)
    
    while q:

        n = len(q)
        for i in range(n):
            temp = q[0]
            del q [0]

            if i == 0 or i == n - 1:
                print(temp.data, end=" ")

            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)