import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from tavoli.models import Tavoli, Fornitore, Cameriere, Prodotti, Spec_Tav, Scontrino, Spec_Scon, Azzeramenti


def index(request):
    """Funzione per l'home page"""

    return render(request, 'index.html')


class TavoliListView(generic.ListView):
    model = Tavoli


class Conto_Tavolo():

    def specifica_tavolo(request, pk):
        """metodo per l'elenco del singolo tavolo"""

        prodotti = Prodotti.objects.all()
        spec_tav = Spec_Tav.objects.filter(tavolo=pk)
        conto = 0
        for spec in spec_tav:
            conto = conto + spec.prodotto.prezzo_vendita

        return render(request, 'tavoli_detail.html',
                      {'prodotti': prodotti, 'spec_tav': spec_tav, 'conto': conto, 'numTav': pk})

    def insert(request, pk, tav):
        create = datetime.datetime.now()
        tavolo = Tavoli.objects.get(id=tav)
        prodotto = Prodotti.objects.get(id=pk)
        cameriere = Cameriere.objects.get(id=2)

        new_article = Spec_Tav(tavolo=tavolo, prodotto=prodotto, cameriere=cameriere, created_at=create)
        new_article.save()

        return HttpResponseRedirect('/tavoli/' + str(tav))

    def delete(request, pk, tav):
        del_article = Spec_Tav.objects.get(id=pk)
        del_article.delete()

        return HttpResponseRedirect('/tavoli/' + str(tav))

    def deleteAll(request, tav):
        del_articles = Spec_Tav.objects.filter(tavolo=tav)
        del_articles.delete()

        return HttpResponseRedirect('/tavoli/' + str(tav))

    def scontrino(request, tav, tipoPag):

        ult_scon = Scontrino.objects.last()
        azz = Azzeramenti.objects.last()

        spec_tav = Spec_Tav.objects.filter(tavolo=tav)
        conto = 0
        for spec in spec_tav:
            conto = conto + spec.prodotto.prezzo_vendita

        num_azz = 1
        num_scont = 1

        if ult_scon is not None:
            if azz is not None:
                if azz.num_azz == ult_scon.num_azz:
                    num_azz = azz.num_azz + 1
                    num_scont = 1
            else:
                num_azz = ult_scon.num_azz
                num_scont = ult_scon.num_azz + 1

        nuovo_scontr = Scontrino(num_azz=num_azz, num_scon=num_scont, tot=conto, tipo_pag=tipoPag)
        nuovo_scontr.save()

        ult_scon = Scontrino.objects.last()

        for spec in spec_tav:
            print(spec.prodotto)
            new_spec_scontr = Spec_Scon(id_scon=ult_scon, id_prodotto=spec.prodotto)
            new_spec_scontr.save()

        Conto_Tavolo.deleteAll(request, tav)

        return HttpResponseRedirect('/tavoli')
