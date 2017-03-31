import random as rand

def gen(n) :
    for total in range(0,n):
        fin = open("./input/{}.in".format(total+1),'w')
        fout = open("./output/{}.out".format(total+1),'w')
        linecount =  rand.randrange(2,101)
        fin.write(str(linecount)+"\n")
        result_name=[]
        result_age=[]
        result_gender=[]
        student_index=[]
        result_school=[]
        for i in range(0,linecount):
            name =""
            age = 0
            length = rand.randrange(1,101)
            for _ in range(0,length):
                name+=chr(rand.randrange(33,126))
            age = rand.randrange(1,201)
            g= rand.randrange(0,100)%2 
            gender=""
            if g==0 : gender+="Male"
            else :gender+="Female"
            result_name.append(name)
            result_age.append(age)
            result_gender.append(gender)
            fin.write(name+" "+str(age)+" "+gender+"\n")
        studentcount = rand.randrange(1,linecount)
        fin.write(str(studentcount)+"\n")
        for i in range(0,studentcount):
            offset = rand.randrange(0,linecount-studentcount)
            name = result_name[offset+i]
            school = ""
            length = rand.randrange(1,101)
            for _ in range(0,length):
                school+=chr(rand.randrange(33,126))
            student_index.append(offset+i)
            result_school.append(school)
            fin.write(name+" "+school+"\n")

        for i in range(0,linecount):
            if i in student_index :
                n=student_index.index(i)
                fout.write(result_name[i]+" is "+str(result_age[i])+" years old, and is "+result_gender[i]+"\n"+result_name[i]+" is studying in "+result_school[n]+"\n")
            else :
                fout.write(result_name[i]+" is "+str(result_age[i])+" years old, and is "+result_gender[i]+"\n")

        fin.close()
        fout.close()


if __name__ == "__main__":
    n=int(input())
    gen(n)




