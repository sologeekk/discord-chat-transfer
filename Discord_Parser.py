import json
import os

Category_Hacking = os.listdir("./Hacking") # Change the Variable name into your foldering format: Category_News = os.listdir("./News")
Category_General = os.listdir("./General Text Channels")

docs = {}
i = 0
messsages_counter = 0
counter_keeper = 0
file_names = []

# Chagne the Alphabets and their values according to your foldering such as 'N':'News',
dict_mapper = {
    'H': 'Hacking',
    'G': 'General Text Channels',
}
keys = dict_mapper.keys()

def retriever(file_Category):
    global i
    global messsages_counter
    global counter_keeper
    file_Cat = file_Category[0][0:1]
    doc_dict_file = {}
    for file_name in file_Category:
        file_names.append(file_name)
        # print(file_names)
        file_path = f"./{dict_mapper[file_Cat]}/{file_name}"
        counter_keeper += i
        i = 0
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            doc_dict_id = {}
            for items in data["messages"]:
                try:
                    if items["embeds"]:
                        i += 1
                    doc_dict_id[i] = {
                        "author": items["author"]["nickname"],
                        "link": items["embeds"][0]["url"],
                    }
                    messsages_counter += 1
                except Exception as e:
                    pass
                
        doc_dict_file[file_name] = doc_dict_id
    messages_counter = {"Message Count": f"{counter_keeper}"}
    doc_dict_file['Message Count'] = messages_counter
    docs[dict_mapper[file_Cat]] = doc_dict_file
    return docs

# Calling retriever
Hacking = retriever(Category_Hacking)
General_Text_chatting = retriever(Category_General)

with open('OutJsonFile.json', 'w') as output:
    json.dump(docs, output, indent=2)


# To Output Data in raw txt format with default foldering format to ease the process of copy pasting content into new discord channels 
def simpleOutPut(parsed_jsonfile):
        newfilenames = []
        try:
            for keys,values in dict_mapper.items():
                parent_path = "./"
                Category_path = f"{keys}"
                Directory = os.path.join(parent_path, Category_path)
                os.mkdir(Directory)


                for filename in file_names:
                    if filename.startswith(keys):
                        newfilenames.append(filename)
                
                    for newfilename in newfilenames:               
                            final_data = []
                            for item in parsed_jsonfile[values][newfilename].values():
                                author = item["author"]
                                link = item["link"]
                                final_data.append(f"{author}:\n{link}")
                            with open(f"{Directory}/{newfilename.replace('json', 'txt')}", 'w') as outfile:
                                outfile.write('\n'.join(final_data))
                    newfilenames.clear()
        except Exception as e:
            pass
                    

# calling simpleoutput
simpleOutPut(Hacking)
simpleOutPut(General_Text_chatting)
