# Chapter 4: Databases

![](images/data.jpeg)

Credit: unknown

## Information vs Database Models

Formal discussions of information might start with the discussion of **information models**. __[Wikipedia's definition](https://en.wikipedia.org/wiki/Information_model)__ reads:

> An information model in software engineering is a representation of concepts and the relationships, constraints, rules, and operations to specify __[data semantics](https://en.wikipedia.org/wiki/Semantic_data_model)__ for a chosen domain of discourse. Typically it specifies relations between kinds of things, but may also include relations with individual things. It can provide sharable, stable, and organized structure of information requirements or knowledge for the domain context.

> An information model provides formalism to the description of a problem domain without constraining how that description is mapped to an actual implementation in software. There may be many mappings of the information model. Such mappings are called data models (...)

Information retrieval then goes a step further and also discusses **information retrieval models**, as does chapter 3 of *Modern Information Retrieval* :

> Modeling in IR is a complex process aimed at producing a ranking function, i.e., a function that assigns scores to documents with regard to a given query. This process consists of two main tasks: (a) the conception of a logical framework for representing documents and queries and (b) the definition of a ranking function that computes a rank for each document with regard to a given query.

> To build a model, we think first of representations of the documents and of the user information needs. In the case of a document, the representation might be a subset of all terms in the document, which can be generated by removing stopwords (such as articles and prepositions) from the text, for instance. In the case of a query the representation might be a superset of the query terms formed by the original query enriched with synonyms, for instance. Given these representations, we then concieve the framework in which they can be modeled.

However, while such models are obviously very interesting for information science, the discussion is also highly theoretical and requires no small amount of mathematics (set theory, algebra, probability theory, ...). Instead, from our practical perspective it makes more sense to open up the discussion of information, by dealing with **database models**. Indeed, in most real-world applications of information science, you will most likely have to deal with specific databases that stores information and not with the abstract information models that map the data to these databases. 


## Databases

__[Wikipedia](https://en.wikipedia.org/wiki/Database)__ defines a database as a "an organized collection of data, generally stored and accessed electronically from a computer system". Such a broad definition allows for many different kinds of databases, ranging from a single text file (e.g. the line `apples,oranges,grapes` is a database!) to complex database management systems (DBMS) like __[MySQL](https://en.wikipedia.org/wiki/MySQL)__ that operate on large data structures.

### Database models

The classification of databases is a topic for a course on its own. For now, it will suffice to say that the development of database technology can be divided into three eras based on data model or structure: navigational, relational/SQL, and post-relational.

#### Navigational

__[Wikipedia](https://en.wikipedia.org/wiki/Navigational_database)__ says

>A navigational database is a type of database in which records or objects are found primarily by following **references from other objects**. The term was popularized by the title of Charles Bachman's 1973 Turing Award paper, The Programmer as Navigator. This paper emphasized the fact that the new disk-based database systems allowed the programmer to choose arbitrary navigational routes following relationships from record to record, contrasting this with the constraints of earlier magnetic-tape and punched card systems where data access was strictly sequential.

(...)

>Although Bachman described the concept of navigation in abstract terms, the idea of navigational access came to be associated strongly with the procedural design of the CODASYL Data Manipulation Language. Writing in 1982, for example, Tsichritzis and Lochovsky state that "The notion of currency is central to the concept of navigation." By the **notion of currency**, they refer to the idea that a program maintains (explicitly or implicitly) a current position in any sequence of records that it is processing, and that operations such as `GET NEXT` and `GET PRIOR` retrieve records relative to this current position, while also changing the current position to the record that is retrieved.

#### Relational/SQL

__[Wikipedia:Relational_model](https://en.wikipedia.org/wiki/Relational_model)__ and __[Wikipedia:Database](https://en.wikipedia.org/wiki/Database)__ say:

>The relational model (...) is an approach to managing data using a structure and language consistent with first-order predicate logic, first described in 1969 by English computer scientist Edgar F. Codd, where all **data is represented in terms of tuples, grouped into relations**. (...) he described a new system for storing and working with large databases. Instead of records being stored in some sort of linked list of free-form records (...), Codd's idea was to organise the data as a number of "tables", each table being used for a different type of entity. Each table would contain a fixed number of columns containing the attributes of the entity. One or more columns of each table were designated as a primary key by which the rows of the table could be uniquely identified; cross-references between tables always used these primary keys, rather than disk addresses, and queries would join tables based on these key relationships, using a set of operations based on the mathematical system of relational calculus (from which the model takes its name). Splitting the data into a set of normalized tables (or relations) aimed to ensure that each "fact" was only stored once, thus simplifying update operations. Virtual tables called views could present the data in different ways for different users, but views could not be directly updated.

>The purpose of the relational model is to provide a declarative method for specifying data and queries: users directly state what information the database contains and what information they want from it, and let the database management system software take care of describing data structures for storing the data and retrieval procedures for answering queries.

>Most relational databases use the SQL data definition and query language

#### Post-relational

__[Wikipedia](https://en.wikipedia.org/wiki/NoSQL)__ says:

>A NoSQL (originally referring to "non-SQL" or "non-relational") database provides a mechanism for storage and retrieval of data that is modeled in **means other than the tabular relations used in relational databases**. Such databases have existed since the late 1960s, but the name "NoSQL" was only coined in the early 21st century (...) NoSQL databases are increasingly used in big data and real-time web applications. NoSQL systems are also sometimes called "Not only SQL" to emphasize that they may support SQL-like query languages or sit alongside SQL databases in polyglot-persistent architectures.

>(...) The data structures used by NoSQL databases (e.g. key–value pair, wide column, graph, or document) are different from those used by default in relational databases, making some operations faster in NoSQL. The particular suitability of a given NoSQL database depends on the problem it must solve. Sometimes the data structures used by NoSQL databases are also viewed as "more flexible" than relational database tables.

Categories of post-relational databases include:

* **key-value stores**, such as the MUMPS database by YottaDB that we use for Brocade, the University of Antwerp's Library Management System
* **document stores**, such as XML or JSON
* **triple stores**, such as RDF

The important thing to realize here is that post-relational databases can express things that relational databases can't. For instance, how would you translate this JSON (postrelational) to a spreadsheet (relational)?

```JSON
{
	"1": {
		"name": "Tom Deneire",
		"age": "39"
	},
	"2": {
		"name": "Gandalf",
		"bio": {
			"age": "unknown",
			"occupation": "wizard"
		}
	}
}
```


### Databases as Linked Data

Another interesting way to think about databases is to consider them from the view point of Linked (open) Data.

At __[w3.org](https://www.w3.org/2011/gld/wiki/5_Star_Linked_Data)__ we read:

>Tim Berners-Lee, the inventor of the Web and initiator of the Linked Data project, suggested a 5 star deployment scheme for Linked Data. The 5 Star Linked Data system is cumulative. Each additional star presumes the data meets the criteria of the previous step(s).

>☆ Data is available on the Web, in whatever format.	

>☆☆ Available as machine-readable structured data, (e.g., not a scanned image).

>☆☆☆ Available in a non-proprietary format, (e.g, CSV, not Microsoft Excel).	

>☆☆☆☆ Published using open standards from the W3C (RDF and SPARQL).	

>☆☆☆☆☆ All of the above and links to other Linked Open Data.

In this way, we can organize different database types into a data hierarchy like such:

![](images/5-star-steps-open-data-5-star-model.png)

* OL: Open License
* RE: Readable
* OF: Open format
* URI: Uniform Resource Identifier
* LD: Linked Data

For a good description of this summary, see __[this article](https://www.ontotext.com/knowledgehub/fundamentals/five-star-linked-open-data/)__.

### RDF

Unfortunately, we do not have time to discuss RDF and Linked Data in detail. However, it is important to realize that RDF is a data model, not a data serialization model, such as XML or JSON - in fact, both can be used to express RDF data.

A quick summary from __[Wikipedia](https://en.wikipedia.org/wiki/Resource_Description_Framework)__:

>The RDF data model is similar to classical conceptual modeling approaches (such as entity–relationship or class diagrams). It is based on the idea of making statements about resources (in particular web resources) in expressions of the form **subject–predicate–object, known as triples**. The subject denotes the resource, and the predicate denotes traits or aspects of the resource, and expresses a relationship between the subject and the object.

>For example, one way to represent the notion "The sky has the color blue" in RDF is as the triple: a subject denoting "the sky", a predicate denoting "has the color", and an object denoting "blue". Therefore, RDF uses subject instead of object (or entity) in contrast to the typical approach of an entity–attribute–value model in object-oriented design: entity (sky), attribute (color), and value (blue).

>RDF is an abstract model with several serialization formats (i.e. file formats), so the particular encoding for resources or triples varies from format to format.

The core concept of the triplestore and the underlying Linked Data principle is the Uniform Resource Identifier (URI), a unique and unambiguous ID for all things linked. Optimally linked data uses URIs for all three elements of the triple, subject, predicate and verb. To illustrate how this works, let's look at the (abbreviated) RDF/XML for the Wikidata entry __[Paris](https://www.wikidata.org/wiki/Q90)__, known as entity `Q90`:

```xml
<?xml version="1.0"?>
    <rdf:Description rdf:about="http://www.wikidata.org/entity/Q90">
        <wdt:P1376 rdf:resource="http://www.wikidata.org/entity/Q142"/>
    </rdf:Description>
```

This is a triple expressing the fact that "Paris" (subject) "is the capital of" (predicate) "France" (object). To express this three URIs are used: `Q90` (Paris), `P1376` (property "is capital of") and `Q142` (France). The makes the statement unique, uniform, unambiguous (telling a computer that Paris the city, not Paris Hilton (Q47899) is the capital of France), and linked: all elements of the triple are linked up to other data, e.g. `Q142` which was the object in this statement, will be the subject of others.

Consider the difference with non-RDF XML where resources are not identified with URIs and data is not linked and the model not open:

```xml
<?xml version="1.0"?>
    <Description>Paris
        <isCapitalof>France</isCapitalof>
    </Description>
```

RDF and especially Linked Open Data are undoubtedly part of the future for information science. If you're interested to know more or need to work with RDF and Linked Data in practice, I highly recommend reading *A Librarian's Guide to Graphs, Data and the Semantic Web*, By James Powell, __[ISBN 978-1843347538](https://isbnsearch.org/isbn/9781843347538)__.

## Query Languages

Database operations can be summarized with the acronym CRUD: create, read, update and delete. From an information standpoint, the main focus is arguably reading from the database. Most often though, we do not read directly as this is not possible (not all databases can be browsed), or practical (we get to much information). Instead, reading databases is usually done through *queries*, for which we use [query languages](https://en.wikipedia.org/wiki/Query_language). 

Actually, query languages surpass databases. Formally, query languages can be classified according to whether they are **database query languages** or **information retrieval query languages**. The difference is that a database query language attempts to give factual answers to factual questions, while an information retrieval query language attempts to find documents containing information that is relevant to an area of inquiry. 

For the latter we will discuss CQL, for the former XML and SQL.

### CQL

Let's start with an example of an information retrieval query language: contextual query language. According to __[Wikipedia](https://en.wikipedia.org/wiki/Contextual_Query_Language)__

>Contextual Query Language (CQL), previously known as Common Query Language, is a formal language for representing queries to information retrieval systems such as search engines, bibliographic catalogs and museum collection information. Based on the semantics of Z39.50, its design objective is that queries be human readable and writable, and that the language be intuitive while maintaining the expressiveness of more complex query languages. It is being developed and maintained by the Z39.50 Maintenance Agency, part of the Library of Congress.

Querying with CQL operates via SRU - Search/Retrieve via URL, which is a standard XML-based protocol for search queries.

You can find the __[SRU](http://www.loc.gov/standards/sru/index.html)__ and __[CQL](https://www.loc.gov/standards/sru/cql/spec.html)__ specifications at the Library of Congress website. 

A fun example of an API that support SRU/CQL is offered by the __[CERL (Consortium of European Research Libraries)](https://cerl.org/)__, which is responsible for the __[CERL Thesaurus](https://data.cerl.org/thesaurus/_search)__, containing forms of imprint places, imprint names, personal names and corporate names as found in material printed before the middle of the nineteenth century - including variant spellings, forms in Latin and other languages, and fictitious names.

To use this API you just send a web request to 

```
https://data.cerl.org/thesaurus/_sru?version=1.2&operation=searchRetrieve&query=
```

followed by your CQL query in double quotes (or rather: `%22` which is the URL-safe encoding entity for `"`), for instance: 

```
https://data.cerl.org/thesaurus/_sru?version=1.2&operation=searchRetrieve&query=%22Erasmus%22
```

The response will be an XML document (database) containing the relevant CERL thesaurus entries for this query.

### XML

XML is something most of you are already familiar with, as it is a recurring technology in digital text analysis. In fact, XML is ubiquitous in the information world. It is very actively used in the library world. Another example is invoicing; for instance, the Government of Flanders has been asking for XML e-invoices from its suppliers for all contracts since 2017.

If you need to brush up your understanding of XML, __[w3schools](https://www.w3schools.com/xml/)__ is a good place to start. Here we will briefly return to the matter of **parsing XML**, which is the process of analyzing XML documents to extract their information.

For Python, two XML libraries are highly recommended:

- __[beautifulsoup](https://pypi.org/project/beautifulsoup4/)__
- __[lxml](https://lxml.de/)__

Both turn XML's hierarchical structure into a parse tree, which behaves like a Pythonic object that you can then iterate over. Chapter 5 will feature a coding assignment that involves parsing and building XML, so it's recommended to refamiliarize yourself with either or both of these libraries.

### SQL/SQLite

Unlike XML, SQL is a technology that is probably new to most of you. Unlike RDF, which libraries seem hesitant to adopt, SQL is ubiquitous, including outside of libraries. Moreover, SQL has for instance heavily influenced the aforementioned CQL, and also __[SPARQL](https://en.wikipedia.org/wiki/SPARQL)__ , the query language for RDF. So knowing SQL will open many doors.

SQL is the query language for RDBMS, which are most often implemented in a *client-server* database engine. So for you to use SQL you would need a connection to a SQL database server, i.e. something like MySQL or Oracle. However, there is also a very good standalone alternative, called __[SQLite](https://en.wikipedia.org/wiki/SQLite)__. Simply said SQLite is just a single file, but you can query it just like a SQL database server. There are some minute differences between SQL syntax and the SQLite dialect, but these are really small.

So let's dive in with this Google Slides __[presentation](https://docs.google.com/presentation/d/1hLpHtKFs79QJYS0NpN9u4RG_hNwqScwoLgObFJKmvy8/edit?usp=sharing)__.

### sqlite3

Python's standard library contains the module __[sqlite3](https://docs.python.org/3/library/sqlite3.html)__ which allows a SQL interface to a database.

For example, let's launch some SQL queries on a sqlite database of __[STCV](https://vlaamse-erfgoedbibliotheken.be/en/dossier/short-title-catalogue-flanders-stcv/stcv)__, which is the Short Title Catalogue Flanders, an online database with extensive bibliographical descriptions of editions printed in Flanders before 1801. This database is available as part of the __[Anet Open Data](https://www.uantwerpen.be/nl/projecten/anet/open-data/)__. A recent version of it is available in this repo under `data`.


import os
import sqlite3

# To use the module, you must first create a Connection object that represents the database
conn = sqlite3.connect(os.path.join('data', 'stcv.sqlite'))
# Once you have a Connection, you create a Cursor object
c = conn.cursor()
# To perform SQL commands you call the Cursor object's excute() method
query = """
        select distinct author_zvwr, title_ti, impressum_ju1sv from author
        join title on author.cloi = title.cloi
        join impressum on title.cloi = impressum.cloi
        group by author_zvwr
        """
c.execute(query)
# Call fetchall() to get a list of the matching rows
# Using list comprehension, explanation at https://medium.com/techtofreedom/8-levels-of-using-list-comprehension-in-python-efc3c339a1f0
data = [row for row in c.fetchall()]
for row in data[50:60]:
    print(row)
# Close the connection when you're done
conn.close()

## Assignment: JSON metadata harvester

### JSON

One (document) database technology which we have not discussed yet, is __[JSON](https://www.json.org/json-en.html)__. If you need to brush up on your JSON skills, __[w3schools](https://www.w3schools.com/js/js_json_intro.asp)__ is again a good starting point. 

However, JSON is much easier to work with than XML. Whereas XML needs to be parsed or queried through __[XPath](https://www.w3schools.com/xml/xpath_intro.asp)__, which is not an easy technology to master, basically, you can just think about JSON as a "string" version (it is a *document* database) of a Python dictionary:
 

json_string = '''
{
	"name": "Deneire",
	"age": 39,
	"initials": ["T", "B"]
}
'''
print(json_string)
print(type(json_string))

python_dict = {}
python_dict["name"] = "Deneire"
python_dict["age"] = 39
python_dict["initials"] = ["T", "B"]
print(python_dict)
print(type(python_dict))

In fact, Python allows you to access JSON just like a database, using the `json` library to either turn JSON into a dict (`loads()` ) or to turn a dict into JSON (`dumps()`):

from json import loads, dumps
contacts = """
{
	"1": {
		"lastname": "Doe",
		"firstname": "John"
	},
	"2": {
		"lastname": "Doe",
		"firstname": "Jane"
	}
}
"""
# Turn JSON into dict with loads()
contacts_dict = loads(contacts)
print(contacts_dict["2"]["lastname"])
# Turn dict into JSON with dumps()
contacts_dict["2"]["lastname"] = "Eyre"
contacts = dumps(contacts_dict)
print(contacts)

### What is an API?

For your assignment you will be using the JSON data made available through the __[Europeana Entities API](https://pro.europeana.eu/page/entity)__, which allows you to search on or retrieve information from named entities. These named entities (such as persons, topics and places) are part of the Europeana Entity Collection, a collection of entities in the context of Europeana harvested from and linked to controlled vocabularies, such as ​Geonames, DBpedia and Wikidata. It is advisable to read the API's __[documentation](https://pro.europeana.eu/page/entity)__ first.

A quick word in general about an __[API](https://en.wikipedia.org/wiki/API)__, or Application Programming Interface.

Non-technical users mostly interact with data through a GUI or Graphical User Interface, either locally (e.g. you use DBbrowser to look at a SQLite database) or on the web (e.g. you use Wikidata's web page). However, when we try to interact with this data from a machine-standpoint, i.e. in programming, this GUI is not suitable. We need an interface that is geared towards computers. So we use a local (e.g. Python's `sqlite3` module) or remote (e.g. __[Wikidata's Query Service](https://query.wikidata.org/)__) API to get this data in a way that can be easily handled by computers.

In this way, an API is an intermediary structure, which has a lot of benefits. Wouldn't it be nicer to have direct access to a certain database? In a way, yes, but this would also cause problems. There are many, many different database architectures, but __[API architectures](https://levelup.gitconnected.com/comparing-api-architectural-styles-soap-vs-rest-vs-graphql-vs-rpc-84a3720adefa)__ are generally quite predictable. They are often based on well-known technologies like JSON or XML, so you don't have to learn a new query language. Moreover, suppose Wikidata changes their database? All of your code that uses the database would need to be rewritten. By using the API intermediary structure Wikidata can change the underlying database, but make sure their API still functions in the same way as before. 

There are lots of free web APIs out there. The __[NASA API](https://api.nasa.gov/)__, for instance, is quite incredible. Or this __[Evil Insult Generator](https://evilinsult.com/generate_insult.php?lang=en&type=json)__, if you want to have some fun! You can find an extensive list of free APIs __[here](https://github.com/public-apis/public-apis).
 

### Assignment

Your assignment is simple. Write a Python script that prompts for user input of a named entity, query the API for that entity, parse the results and print them on standard output.

#### Some tips:

- You can use the key `wskey=apidemo` for your API request.
- A good Python library to access URLs is `urllib`, an alternative (which is not in the standard library) is `requests`.
- Think about what we have seen already about standardizing/normalizing search strings, but take this to the next level.
- Try to anticipate what can go wrong so the program doesn't crash in unexpected situations.
- Test your application with the following search strings: `Erasmus`, `Justus Lipsius` and `Django Spirelli`.

If this is an easy task for you, you might think about parsing the results and adding them to your own database structure, e.g. XML or SQLite. 


