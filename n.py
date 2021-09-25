{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0884b7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "a=[]\n",
    "s=int(input(\"enter size\"))\n",
    "for i in range(s):\n",
    "    v=input(\"enter val\")\n",
    "    a.append(v)\n",
    "for i in range (s):\n",
    "    print(a[i])\n",
    "print(len(a))\n",
    "print(max(a))\n",
    "g=a.count(int(input(\"enter to count\")))\n",
    "print(g)\n",
    "f=a.index(int(input(\"enter index\")))\n",
    "print(f)\n",
    "h=a.insert(int(input(\"enter the index\")),input(\"enter item\"))\n",
    "print(a)\n",
    "i=a.remove(input(\"enter item top del\"))\n",
    "print(a)\n",
    "a.sort()\n",
    "print(a)\n",
    "a.pop()\n",
    "print(a)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
