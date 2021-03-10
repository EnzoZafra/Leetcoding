class Node:
    def __init__(self):
        self.files = {}
        self.isFile = False
        self.content = ''

class FileSystem:

    def __init__(self):
        self.root = Node()

    def ls(self, path: str) -> List[str]:
        curr = self.root
        out = []
        
        if path != '/':
            path_split = path.split('/')
            for path in path_split[1:]:
                curr = curr.files[path]
            
            if curr.isFile:
                out.append(path_split[-1])
                return out
        out = curr.files.keys() 
        return sorted(out)

    def mkdir(self, path: str) -> None:
        curr = self.root
        path_split = path.split('/')
        for path in path_split[1:]:
            if path not in curr.files:
                new_node = Node()
                curr.files[path] = new_node
                curr = new_node
            else:
                curr = curr.files[path]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_split = filePath.split('/')
        curr = self.root
        
        # traverse to directory
        for path in path_split[1:-1]:
            curr = curr.files[path]
        
        file_name = path_split[-1]
        if file_name not in curr.files:
            new_file = Node()
            curr.files[file_name] = new_file
        
        file = curr.files[file_name]
        file.isFile = True
        file.content = file.content + content
         
    def readContentFromFile(self, filePath: str) -> str:
        path_split = filePath.split('/')
        curr = self.root
        
        for path in path_split[1:-1]:
            curr = curr.files[path]
        
        file_name = path_split[-1]
        return curr.files[file_name].content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)