#include <bits/stdc++.h>
using namespace std;

int main(){
  set<pair<string, string> > books;
  set<pair<string, string> > books_return;
  map<string, string> authors;
  string line;
  smatch sm;
  regex e1("\"([^\"]+)\" by (.+)");
  while (true){
    getline(cin, line);
    if (line == "END") break;
    regex_match(line, sm, e1);
    books.emplace(sm[2], sm[1]);
    authors[sm[1]] = sm[2];
  }

  regex e2("(\\w+)(?: \"([^\"]+)\")?");
  while (true){
    getline(cin, line);
    if (line == "END") break;
    regex_match(line, sm, e2);
    if (sm[1] == "BORROW"){
      pair<string, string> b(authors[sm[2]], sm[2]);
      books_return.erase(b) || books.erase(b);
    } else if (sm[1] == "RETURN"){
      books_return.emplace(authors[sm[2]], sm[2]);
    } else if (sm[1] == "SHELVE"){
      for (auto it=books_return.begin(); it!=books_return.end(); ++it){
        auto prev = books.emplace(it->first, it->second);
        if (prev.first != books.begin()){
          --prev.first;
          printf("Put \"%s\" after \"%s\"\n", it->second.c_str(), prev.first->second.c_str());
        } else {
          printf("Put \"%s\" first\n", it->second.c_str());
        }
      }
      cout << "END\n";
      books_return.clear();
    }
  }

  return 0;
}
